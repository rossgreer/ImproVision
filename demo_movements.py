### DEMONSTRATION OF ONE MEASURE OF MOVEMENTS ###

import pretty_midi
import time
import cv2
import numpy as np
import requests
from mmpose.apis import MMPoseInferencer, init_model, inference_topdown
import matplotlib.pyplot as plt
import time

# Constants
INSTRUMENT_ORDER = ['Violin I', 'Violin II', 'Viola', 'Violoncello']
#CAMERA_URL = 'http://192.168.100.88/cgi-bin/ptzctrl.cgi?ptzcmd&'
MIDI_FILE_NAME = 'next_right_thing_2.mid'
DEVICE = 'cuda'
CAMERA_IP = "192.168.100.88"
BASE_URL = f'http://{CAMERA_IP}/cgi-bin/ptzctrl.cgi?ptzcmd&'

def robot_instructions(midi_file_name):
    """
    Analyzes a MIDI file to prepare measure-by-measure signaling instructions for a robot.
    
    Parameters:
    midi_file_name (str): The path to the MIDI file to be analyzed. Currently assumed to be in 4/4 time at 120 bpm.
    Arbitrary number of instruments and measures.
    
    Returns:
    A list of dictionaries, each representing a measure and containing instruments with their movements. 
    """
    midi_data = pretty_midi.PrettyMIDI(midi_file_name)
    instructions = []

    for instrument in midi_data.instruments:
        if not instrument.is_drum: # Skip drums, MIDI treats those weirdly
            previous_pitch = None
            previous_measure = None

            for note in sorted(instrument.notes, key=lambda x: x.start):
                # Assuming 4/4 time signature and 120 bpm
                measure_number = int(note.start / (60 / 120) / 4) + 1 # 60/120/4 because 60secs/120bpm in 4/4 time

                if previous_pitch is not None and previous_measure is not None and measure_number != previous_measure:
                    pitch_difference = note.pitch - previous_pitch
                    movement = determine_robot_movement(pitch_difference)

                    while len(instructions) < measure_number - 1:
                        instructions.append({}) # Add a new dictionary for each new measure

                    instrument_name = instrument.name or f"Program {instrument.program}"
                    instructions[measure_number - 2][instrument_name] = movement # -2 because we skip the first measure (i.e., moving into measure 1) & list indexing

                previous_pitch = note.pitch
                previous_measure = measure_number
    
    return instructions

def determine_robot_movement(pitch_difference):
    """Determines the movement for the robot based on pitch difference."""
    if pitch_difference == 0:
        return "stay"
    elif pitch_difference == 1:
        return "up half"
    elif pitch_difference == 2:
        return "up whole"
    elif pitch_difference == -1:
        return "down half"
    elif pitch_difference == -2:
        return "down whole"
    else:
        return "irregular"

def send_camera_control(command, pan_speed=24, tilt_speed=20, focus_speed=10, zoom_speed=10): # updated to include speed parameter
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
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Command '{command}' was successful")
        return "success"
    else:
        print(f"Failed to execute command '{command}'")
        return "failure"

def simple_execute_one_measure(midi_file_name, measure_number): # just for now, use actual positions later
    instructions_by_measure = robot_instructions(midi_file_name)

    if measure_number < 1 or measure_number > len(instructions_by_measure):
        print(f"Measure number {measure_number} is out of range for the given MIDI file.")
        return

    measure_instructions = instructions_by_measure[measure_number - 1]

    # Center
    send_camera_control("home")
    time.sleep(1)

    ### REPLACE: find person on far left ###
    # Start by panning to the far left
    send_camera_control("left")  
    time.sleep(1)  # Wait a bit
    send_camera_control("ptzstop")  # Stop the camera movement

    # Iterate over instruments in order
    for instrument in INSTRUMENT_ORDER:
        time.sleep(.5)
        movement = measure_instructions.get(instrument)
        if movement:
            print(f"Executing movement for {instrument}: {movement}")
            execute_movement_for_instrument(movement) # See helper function below
        else:
            print(f"{instrument} has no specific movement. 'Looking' at the instrument.")
            time.sleep(1)
        
        time.sleep(0.5)

        # Pan to the next instrument on the right
        if instrument != INSTRUMENT_ORDER[-1]:
            ### REPLACE: find next person towards the right ###
            send_camera_control("right")
            time.sleep(.75)  
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

def execute_movement_for_instrument(movement): # only used for simple_execute_one_measure
    """
    Executes the camera movement based on the specified movement instruction.

    Parameters:
    movement (str): The movement instruction (e.g., "up half", "up whole").
    """
    if movement == "up half":
        send_camera_control("up")
        time.sleep(0.7)
        send_camera_control("ptzstop")
        # Return to horizontal
        time.sleep(0.7)
        send_camera_control("down")
        time.sleep(0.6)
        send_camera_control("ptzstop")
    elif movement == "up whole":
        send_camera_control("up")
        time.sleep(0.6)
        send_camera_control("ptzstop")
        time.sleep(0.5)  # Pause between half steps
        send_camera_control("up")
        time.sleep(0.6)
        send_camera_control("ptzstop")
        # Return to horizontal
        time.sleep(0.7)
        send_camera_control("down")
        time.sleep(0.75)
        send_camera_control("ptzstop")
    elif movement == "down half":
        send_camera_control("down")
        time.sleep(0.7)
        send_camera_control("ptzstop")
        # Return to horizontal
        time.sleep(0.7)
        send_camera_control("up")
        time.sleep(0.7)
        send_camera_control("ptzstop")
    elif movement == "down whole":
        send_camera_control("down")
        time.sleep(0.5)
        send_camera_control("ptzstop")
        time.sleep(0.5)  # Pause between half steps
        send_camera_control("down")
        time.sleep(0.5)
        send_camera_control("ptzstop")
        # Return to horizontal
        time.sleep(0.7)
        send_camera_control("up")
        time.sleep(0.7)
        send_camera_control("ptzstop")


# to demonstrate what the execution of one measure of instructions looks like
simple_execute_one_measure(MIDI_FILE_NAME, 4)