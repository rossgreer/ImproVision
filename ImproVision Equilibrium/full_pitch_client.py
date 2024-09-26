import socket
import re
from typing import List, Tuple
import math
import itertools
import requests
import time


DEVICE = 'cuda'
CAMERA_IP = "192.168.100.88"
BASE_URL = f'http://{CAMERA_IP}/cgi-bin/ptzctrl.cgi?ptzcmd&'


### CHORD ANALYSIS FUNCTIONS ###

def parse_note(note_str: str) -> Tuple[str, int]:
    match = re.match(r"([A-G]#?)(\d)", note_str)
    if not match:
        raise ValueError(f"Invalid note format: {note_str}")
    note, octave = match.groups()
    return note, int(octave)

def parse_and_sort_detected_notes(notes_data: str) -> List[str]:
    pattern = r'([A-G]#?\d) \((\d+\.\d+) Hz\)'
    matches = re.findall(pattern, notes_data)
    
    # Sort the matches by frequency
    sorted_matches = sorted(matches, key=lambda x: float(x[1]))
    
    # Return only the sorted note names
    return [match[0] for match in sorted_matches]

def note_to_freq(note: str, octave: int) -> float:
    note_freqs = {
        'C': 16.35, 'C#': 17.32, 'D': 18.35, 'D#': 19.45,
        'E': 20.60, 'F': 21.83, 'F#': 23.12, 'G': 24.50,
        'G#': 25.96, 'A': 27.50, 'A#': 29.14, 'B': 30.87
    }
    return note_freqs[note] * (2 ** octave)

def calculate_interval(freq1: float, freq2: float) -> float:
    return 12 * math.log2(freq2 / freq1)

def is_consonant(interval: float) -> bool:
    consonant_intervals = {0, 3, 4, 5, 7, 8, 9, 12}  # Unison, 3rds, 4ths, 5ths, 6ths, Octave
    rounded_interval = round(interval) % 12
    return rounded_interval in consonant_intervals

def evaluate_chord_consonance(notes: List[str]) -> bool:
    parsed_notes = [parse_note(note) for note in notes]
    
    for i in range(len(parsed_notes)):
        for j in range(i + 1, len(parsed_notes)):
            note1, octave1 = parsed_notes[i]
            note2, octave2 = parsed_notes[j]
            freq1 = note_to_freq(note1, octave1)
            freq2 = note_to_freq(note2, octave2)
            interval = calculate_interval(freq1, freq2)
            
            if not is_consonant(interval):
                return False
    
    return True

def note_to_number(note: str) -> int:
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    note_name, octave = note[:-1], int(note[-1])
    return note_names.index(note_name) + 12 * octave

def number_to_note(number: int) -> str:
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = number // 12
    note_name = note_names[number % 12]
    return f"{note_name}{octave}"

def calculate_movement(original_note: str, new_note: str) -> int:
    original_number = note_to_number(original_note)
    new_number = note_to_number(new_note)
    return abs(new_number - original_number)

def movement_description(delta: int) -> str:
    if delta == 0:
        return "stay"
    elif delta == 1:
        return "up half"
    elif delta == 2:
        return "up whole"
    elif delta == -1:
        return "down half"
    elif delta == -2:
        return "down whole"
    else:
        raise ValueError("Unexpected delta value")

def calculate_note_movements(original_chord: List[str], final_chord: List[str]) -> List[str]:
    original_numbers = [note_to_number(note) for note in original_chord]
    final_numbers = [note_to_number(note) for note in final_chord]
    
    movements = []
    for orig, final in zip(original_numbers, final_numbers):
        delta = final - orig
        description = movement_description(delta)
        movements.append(description)
    
    return movements

def generate_variations(original_chord: List[str]) -> Tuple[List[str], int, List[str]]:
    variations = set()

    original_numbers = [note_to_number(note) for note in original_chord]
    
    all_variations = []
    for num in original_numbers:
        note_variations = [num]
        for delta in [-2, -1, 0, 1, 2]:
            new_num = num + delta
            note_variations.append(new_num)
        all_variations.append(note_variations)
    
    for combination in itertools.product(*all_variations):
        chord_variation = [number_to_note(num) for num in combination]
        if any(note != original_note for note, original_note in zip(chord_variation, original_chord)):
            total_movement = sum(calculate_movement(orig, new) for orig, new in zip(original_chord, chord_variation))
            if evaluate_chord_consonance(chord_variation):
                variations.add((tuple(chord_variation), total_movement))
    
    variations = list(variations)
    
    if not variations:
        return None

    min_movement = min(variations, key=lambda x: x[1])[1]
    
    min_variations = [v for v in variations if v[1] == min_movement]
    
    original_notes_set = set(original_chord)
    
    variations_with_new_notes = [var for var in min_variations if any(note not in original_notes_set for note in var[0])]
    
    if variations_with_new_notes:
        final_variation = min(variations_with_new_notes, key=lambda x: x[1])
    else:
        final_variation = min(min_variations, key=lambda x: x[1])
    
    final_chord, final_movement = final_variation
    note_movements = calculate_note_movements(original_chord, final_chord)
    
    return final_chord, final_movement, note_movements




### CAMERA CONTROL FUNCTIONS ###

def send_camera_control(command, pan_speed=24, tilt_speed=20, focus_speed=10, zoom_speed=10):
    """
    Sends a command to the camera with optional speed parameters and checks the response status.
    """
    def build_cgi_url(command, pan_speed, tilt_speed, focus_speed, zoom_speed):
        """
        Constructs the camera control URL based on the command and speeds provided.
        """
        action = command.lower()
        if action in ["up", "down", "left", "right"]:
            return f"{BASE_URL}{action}&{pan_speed}&{tilt_speed}"
        elif action in ["home", "ptzstop"]:
            return f"{BASE_URL}{action}"
        elif action in ["focusin", "focusout", "focusstop"]:
            return f"{BASE_URL}{action}&{focus_speed}"
        elif action in ["zoomin", "zoomout", "zoomstop"]:
            return f"{BASE_URL}{action}&{zoom_speed}"
        else:
            return f"{BASE_URL}home&10&10"

    url = build_cgi_url(command, pan_speed, tilt_speed, focus_speed, zoom_speed)
    #print(f"Sending camera command: {url}")  # Print the URL for debugging
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Command '{command}' was successful")
        return "success"
    else:
        print(f"Failed to execute command '{command}'")
        return "failure"

def execute_movement_for_instrument(movement):
    #print(f"Executing movement: {movement}")  # Print the movement being executed
    if movement == "up half":
        send_camera_control("up")
        time.sleep(0.7)
        send_camera_control("ptzstop")
        time.sleep(0.7)
        send_camera_control("down")
        time.sleep(0.6)
        send_camera_control("ptzstop")
    elif movement == "up whole":
        send_camera_control("up")
        time.sleep(0.6)
        send_camera_control("ptzstop")
        time.sleep(0.5)
        send_camera_control("up")
        time.sleep(0.6)
        send_camera_control("ptzstop")
        time.sleep(0.7)
        send_camera_control("down")
        time.sleep(0.75)
        send_camera_control("ptzstop")
    elif movement == "down half":
        send_camera_control("down")
        time.sleep(0.7)
        send_camera_control("ptzstop")
        time.sleep(0.7)
        send_camera_control("up")
        time.sleep(0.7)
        send_camera_control("ptzstop")
    elif movement == "down whole":
        send_camera_control("down")
        time.sleep(0.5)
        send_camera_control("ptzstop")
        time.sleep(0.5)
        send_camera_control("down")
        time.sleep(0.5)
        send_camera_control("ptzstop")
        time.sleep(0.7)
        send_camera_control("up")
        time.sleep(0.7)
        send_camera_control("ptzstop")
    elif movement == "stay":
        # No movement required
        time.sleep(1)
    print(f"Finished executing movement: {movement}")  

def execute_chord_movements(chord, movements):
    # Center
    send_camera_control("home")
    time.sleep(1)

    # Start by panning to the far left
    send_camera_control("left")  
    time.sleep(0.7)
    send_camera_control("ptzstop")

    # Iterate over notes in the chord
    for i, (note, movement) in enumerate(zip(chord, movements)):
        time.sleep(0.5)
        print(f"Executing movement for {note}: {movement}")
        execute_movement_for_instrument(movement)
        
        time.sleep(0.5)
        
        # Pan to the next note position on the right
        if i < len(chord) - 1:
            send_camera_control("right")
            time.sleep(0.5)  
            send_camera_control("ptzstop")
    
    # Final 'slam' cue
    send_camera_control("home")
    time.sleep(2)
    send_camera_control('ptzstop')
    time.sleep(0.5)
    send_camera_control('up')
    time.sleep(0.7)
    send_camera_control('down')
    time.sleep(1.5)
    send_camera_control('ptzstop')
    time.sleep(2)
    send_camera_control('home')
    time.sleep(1)

def main():
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 8080         # The port used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            print(f"Connecting to server at {HOST}:{PORT}")
            s.connect((HOST, PORT))
            print("Connected to server")
            full_data = ""
            while True:
                data = s.recv(1024).decode('utf-8')
                if not data:
                    break
                full_data += data
                
                if "DETECTED_NOTES" in full_data and "END_DETECTED_NOTES" in full_data:
                    notes_start = full_data.index("DETECTED_NOTES") + len("DETECTED_NOTES") + 1
                    notes_end = full_data.index("END_DETECTED_NOTES")
                    notes_data = full_data[notes_start:notes_end].strip()
                    
                    # Save raw notes to a file
                    with open('detected_notes.txt', 'w') as f:
                        f.write(notes_data)
                    print("Detected notes saved to detected_notes.txt")
                    
                    # Print detected notes
                    print("Detected notes (unsorted):")
                    print(notes_data)
                    
                    # Parse and sort the notes for chord analysis
                    original_chord = parse_and_sort_detected_notes(notes_data)
                    print(f"\nParsed and sorted chord for analysis: {original_chord}")
                    
                    # Perform chord analysis
                    result = generate_variations(original_chord)
                    if result:
                        variation, total_movement, note_movements = result
                        print(f"\nVariation with lowest total semitone movement: {variation}")
                        print(f"Total Semitone Movement: {total_movement}")
                        print("\nMovements for each note:")
                        for original, new, movement in zip(original_chord, variation, note_movements):
                            print(f"Move {original} to {new}: {movement}")
                        
                        print("\nStarting camera movements:")
                        execute_chord_movements(variation, note_movements)
                    else:
                        print("\nNo consonant variations found.")
                    
                    full_data = full_data[notes_end + len("END_DETECTED_NOTES"):]
                if "\n\nEND\n\n" in full_data:
                    break
            print("Sending acknowledgment")
            s.sendall(b"ACK")
            print("Acknowledgment sent")
        except ConnectionRefusedError:
            print(f"Connection to {HOST}:{PORT} was refused. Is the server running?")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()