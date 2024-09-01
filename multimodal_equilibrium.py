import socket
import re
from typing import List, Tuple
import math
import itertools
import requests
import time
import cv2
import numpy as np
from mmpose.apis import init_model, inference_topdown
import sys
from itertools import product


# Constants
DEVICE = 'cuda'
CAMERA_IP = "192.168.100.88"
BASE_URL = f'http://{CAMERA_IP}/cgi-bin/ptzctrl.cgi?ptzcmd&'
HAND_RAISE_THRESHOLD = 50  # Adjust this value as needed (increased for more significant raise)
HEAD_PROXIMITY_THRESHOLD = 100  # Adjust this value as needed


### POSE FUNCTIONS ###

def init_pose_model():
    """
    Initializes the pose model for human pose estimation.
    """
    model_cfg = '/home/cvrr/mmpose/configs/body_2d_keypoint/rtmpose/coco/rtmpose-m_8xb64-270e_coco-wholebody-256x192.py'
    ckpt = 'https://download.openmmlab.com/mmpose/v1/projects/rtmposev1/rtmpose-m_simcc-coco-wholebody_pt-aic-coco_270e-256x192-cd5e845c_20230123.pth'
    return init_model(model_cfg, ckpt, device=DEVICE)

def draw_keypoints(frame, keypoints, color=(0, 255, 0)):
    for i, keypoint in enumerate(keypoints):
        if len(keypoint) > 2 and keypoint[2] > 0.5:
            cv2.circle(frame, (int(keypoint[0]), int(keypoint[1])), 3, color, -1)
            cv2.putText(frame, str(i), (int(keypoint[0]), int(keypoint[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        elif len(keypoint) == 2:
            cv2.circle(frame, (int(keypoint[0]), int(keypoint[1])), 3, color, -1)
            cv2.putText(frame, str(i), (int(keypoint[0]), int(keypoint[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

def detect_gestures(keypoints):
    """
    Detects two gestures: Raised Hand (significantly above nose) and Hand to Head
    """
    nose = keypoints[0]
    left_wrist = keypoints[9]
    right_wrist = keypoints[10]
    
    # Detect Raised Hand (significantly above nose)
    left_hand_raised = left_wrist[1] < nose[1] - HAND_RAISE_THRESHOLD
    right_hand_raised = right_wrist[1] < nose[1] - HAND_RAISE_THRESHOLD
    
    # Detect Hand to Head
    left_hand_to_head = np.linalg.norm(np.array(left_wrist[:2]) - np.array(nose[:2])) < HEAD_PROXIMITY_THRESHOLD
    right_hand_to_head = np.linalg.norm(np.array(right_wrist[:2]) - np.array(nose[:2])) < HEAD_PROXIMITY_THRESHOLD
    
    return (left_hand_raised or right_hand_raised), (left_hand_to_head or right_hand_to_head)

def process_video_stream(cap, model):
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame from camera. Attempting Camera Stream restart.")
            cap.release()
            cv2.destroyAllWindows()
            while not cap.isOpened():
                cap = cv2.VideoCapture(f'rtsp://{CAMERA_IP}/1')
                if cap.isOpened():
                    ret, frame = cap.read()
                else:
                    print("Error: Couldn't open the camera. Attempting restart.")
                    time.sleep(1)

        if time.time() - start_time < 3:
            cv2.imshow('Camera Stream', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            continue  # Skip detection for the first 3 seconds

        result = inference_topdown(model, frame)
        if len(result) > 0:
            for person in result:
                keypoints = person.pred_instances.keypoints[0]
                draw_keypoints(frame, keypoints)

                hand_raised, hand_to_head = detect_gestures(keypoints)

                if hand_raised and not hand_to_head:
                    print("Hand Raised detected!")
                    return "Hand Raised"
                elif hand_to_head and not hand_raised:
                    print("Hand to Head detected!")
                    return "Hand to Head"

        cv2.imshow('Camera Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return None  # Return None if the loop exits without detecting a gesture



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

# Mapping of note names to MIDI numbers
NOTE_TO_MIDI = {
    'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5, 
    'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
}

MIDI_TO_NOTE = {
    0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 
    6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'
}

def note_to_midi(note):
    """Convert a note name (e.g., 'C4') to MIDI number."""
    octave = int(note[-1])
    pitch_class = note[:-1]
    return NOTE_TO_MIDI[pitch_class] + (octave + 1) * 12

def midi_to_note(midi):
    """Convert a MIDI number to note name."""
    octave = (midi // 12) - 1
    pitch_class = MIDI_TO_NOTE[midi % 12]
    return f"{pitch_class}{octave}"

def identify_chord(notes):
    pitches = [note_to_midi(note) % 12 for note in notes]
    unique_pitches = sorted(set(pitches))
    
    if len(unique_pitches) < 3:
        return "Not enough unique pitches for a triad"
    
    intervals = np.diff(unique_pitches)
    
    if np.array_equal(intervals, [4, 3]) or np.array_equal(intervals, [3, 5]) or np.array_equal(intervals, [5, 4]):
        return "Major"
    
    if np.array_equal(intervals, [3, 4]) or np.array_equal(intervals, [4, 5]) or np.array_equal(intervals, [5, 3]):
        return "Minor"
    
    return "Neither major nor minor triad"

def find_closest_constrained_chord(notes, desired_quality, max_movement=2):
    base_pitches = np.array([note_to_midi(note) for note in notes])
    num_musicians = len(notes)
    
    best_match = None
    min_cost = float('inf')
    
    movements = list(product(range(-max_movement, max_movement + 1), repeat=num_musicians))
    
    for movement in movements:
        new_pitches = base_pitches + np.array(movement)
        normalized_pitches = new_pitches % 12
        
        if desired_quality == "Major":
            if set(normalized_pitches) == set([0, 4, 7]):  # Major triad
                cost = sum(abs(m) for m in movement)
                if cost < min_cost:
                    min_cost = cost
                    best_match = new_pitches
        elif desired_quality == "Minor":
            if set(normalized_pitches) == set([0, 3, 7]):  # Minor triad
                cost = sum(abs(m) for m in movement)
                if cost < min_cost:
                    min_cost = cost
                    best_match = new_pitches
    
    if best_match is not None:
        return [midi_to_note(pitch) for pitch in best_match], min_cost
    else:
        return None, float('inf')




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
    model = init_pose_model()
    cap = cv2.VideoCapture(f'rtsp://{CAMERA_IP}/1')
    if not cap.isOpened():
        print("Error: Couldn't open the camera.")
        sys.exit(1)

    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 8080         # The port used by the server

    detected_gesture = None
    while detected_gesture is None:
        detected_gesture = process_video_stream(cap, model)

    desired_quality = "Major" if detected_gesture == "Hand Raised" else "Minor"
    print(f"Detected gesture: {detected_gesture}. Moving to {desired_quality} chord.")

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

                    # Find closest constrained chord based on the detected gesture
                    closest_chord, total_movement = find_closest_constrained_chord(original_chord, desired_quality)
                    
                    if closest_chord:
                        print(f"\nClosest {desired_quality} chord: {closest_chord}")
                        print(f"Total Semitone Movement: {total_movement}")

                        # Calculate movements for each note
                        note_movements = []
                        for original, new in zip(original_chord, closest_chord):
                            semitone_diff = note_to_midi(new) - note_to_midi(original)
                            if semitone_diff == 0:
                                movement = "stay"
                            elif semitone_diff > 0:
                                movement = "up whole" if semitone_diff == 2 else "up half"
                            else:
                                movement = "down whole" if semitone_diff == -2 else "down half"
                            note_movements.append(movement)

                        print("\nMovements for each note:")
                        for original, new, movement in zip(original_chord, closest_chord, note_movements):
                            print(f"Move {original} to {new}: {movement}")

                        print("\nStarting camera movements:")
                        execute_chord_movements(closest_chord, note_movements)
                    else:
                        print(f"\nNo {desired_quality} chord variation found within constraints.")

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

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()