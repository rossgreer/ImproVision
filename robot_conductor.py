import pretty_midi
import time
import cv2
import numpy as np
import requests
from mmpose.apis import MMPoseInferencer, init_model, inference_topdown

# Constants
INSTRUMENT_ORDER = ['Violin I', 'Violin II', 'Viola', 'Violoncello']
CAMERA_URL = 'http://192.168.100.88/cgi-bin/ptzctrl.cgi?ptzcmd&'
MIDI_FILE_NAME = 'next_right_thing_2.mid'
DEVICE = 'cuda'

def robot_instructions(midi_file_name):
    """
    Analyzes a MIDI file to prepare measure-by-measure signaling instructions for the robot.
    """
    midi_data = pretty_midi.PrettyMIDI(midi_file_name)
    instructions = []

    for instrument in midi_data.instruments:
        if not instrument.is_drum:
            previous_pitch = None
            previous_measure = None

            for note in sorted(instrument.notes, key=lambda x: x.start):
                measure_number = int(note.start / (60 / 120) / 4) + 1

                if previous_pitch is not None and previous_measure is not None and measure_number != previous_measure:
                    pitch_difference = note.pitch - previous_pitch
                    movement = determine_robot_movement(pitch_difference)

                    while len(instructions) < measure_number - 1:
                        instructions.append({})

                    instrument_name = instrument.name or f"Program {instrument.program}"
                    instructions[measure_number - 2][instrument_name] = movement

                previous_pitch = note.pitch
                previous_measure = measure_number

    return instructions

def determine_robot_movement(pitch_difference):
    """
    Determines the movement for the robot based on pitch difference. Helper function for robot_instructions.
    """
    movements = {
        0: "stay",
        1: "up half",
        2: "up whole",
        -1: "down half",
        -2: "down whole"
    }
    return movements.get(pitch_difference, "irregular")

def send_camera_control(command):
    """
    Sends a command to the camera and checks the response status. 
    """
    url = CAMERA_URL + command
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Command '{command}' was successful")
    else:
        print(f"Failed to execute command '{command}'")

def execute_movement(movement):
    """
    Executes the camera movement based on the specified movement instruction.
    """
    movements = {
        "up half": ("up", 0.7),
        "up whole": [("up", 0.5), ("up", 0.5)],
        "down half": ("down", 0.7),
        "down whole": [("down", 0.5), ("down", 0.5)]
    }
    commands = movements.get(movement)
    if commands:
        if isinstance(commands, list): # If multiple commands per movement (i.e., whole steps)
            for cmd, delay in commands:
                send_camera_control(cmd)
                time.sleep(delay)
                send_camera_control("ptzstop")
        else:
            cmd, delay = commands
            send_camera_control(cmd)
            time.sleep(delay)
            send_camera_control("ptzstop")
    time.sleep(2)
    send_camera_control("home")
    time.sleep(2)

def execute_one_measure(midi_file_name, measure_number, musician_positions):
    """
    Executes camera movements based on the instructions extracted from a specific measure in the given MIDI file.
    """
    instructions_by_measure = robot_instructions(midi_file_name)
    if measure_number < 1 or measure_number > len(instructions_by_measure):
        print(f"Measure number {measure_number} is out of range.")
        return

    measure_instructions = instructions_by_measure[measure_number - 1]
    send_camera_control("home") # Center
    time.sleep(4)

    for instrument in INSTRUMENT_ORDER:
        if instrument in musician_positions:
            x_pos = musician_positions[instrument]
            move_time, direction = time_for_turn_by_proportion_of_range(x_pos)
            send_camera_control(direction)
            time.sleep(move_time)
            send_camera_control("ptzstop")

            time.sleep(1)
            movement = measure_instructions.get(instrument)
            if movement:
                print(f"Executing movement for {instrument}: {movement}")
                execute_movement(movement) # See helper function above
            else:
                print(f"{instrument} has no specific movement.")
                time.sleep(1)

            # Pan to the next musician
            if instrument != INSTRUMENT_ORDER[-1]:
                next_instrument = INSTRUMENT_ORDER[INSTRUMENT_ORDER.index(instrument) + 1]
                if next_instrument in musician_positions:
                    next_x_pos = musician_positions[next_instrument]
                    next_move_time, next_direction = time_for_turn_by_proportion_of_range(next_x_pos)
                    send_camera_control(next_direction)
                    time.sleep(next_move_time)
                    send_camera_control("ptzstop")

    # Final slam cue
    send_camera_control("home")
    time.sleep(3)
    send_camera_control("ptzstop")
    time.sleep(1)
    send_camera_control("up")
    time.sleep(0.7)
    send_camera_control("down")
    time.sleep(0.7)

def time_for_turn_by_proportion_of_range(target_nose_x):
    """
    Calculates the duration and direction for the camera to turn based on the target nose x-coordinate.
    """
    left_range = .62 
    right_range = .56
    max_x_left = 301/1920
    max_x_right = 1736/1920
    rate_left = (1920/2 - 301)/.62  
    rate_right = (1736 - 1920/2)/.56  

    if target_nose_x > 1920/2:
        direction = "right"
        target_motion_time = (target_nose_x - 1920/2) /  rate_right
    else:
        direction = "left"
        target_motion_time = (1920/2 - target_nose_x) / rate_left

    return target_motion_time, direction

def init_pose_model():
    """
    Initializes the pose model for human pose estimation.
    """
    model_cfg = '/home/cvrr/mmpose/configs/body_2d_keypoint/rtmpose/coco/rtmpose-m_8xb64-270e_coco-wholebody-256x192.py'
    ckpt = 'https://download.openmmlab.com/mmpose/v1/projects/rtmposev1/rtmpose-m_simcc-coco-wholebody_pt-aic-coco_270e-256x192-cd5e845c_20230123.pth'
    return init_model(model_cfg, ckpt, device=DEVICE)

def is_hand_above_head(person_landmarks):
    """
    Checks if any hand is raised above the head.
    """
    nose_y = person_landmarks['nose'][1]
    left_wrist_y = person_landmarks['left_wrist'][1]
    right_wrist_y = person_landmarks['right_wrist'][1]
    return left_wrist_y < nose_y or right_wrist_y < nose_y

def get_musician_positions(results):
    """
    Extracts the positions of the musicians from the pose estimation results.
    """
    positions = {}
    for person in results:
        keypoints = person['keypoints']
        person_landmarks = {
            'nose': keypoints[0],
            'left_wrist': keypoints[9],
            'right_wrist': keypoints[10]
        }
        nose_x = person_landmarks['nose'][0]
        positions[person['bbox'][0][0]] = nose_x  # Map bbox x-coordinate to instrument name
    return positions

def process_video_stream(cap, model, instructions):
    """
    Processes the video stream to detect hand-raising gestures and execute movements.
    """
    measure_number = 1  # Initialize measure number
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame from camera.")
            break

        result = inference_topdown(model, frame)
        if len(result['predictions']) > 0:
            musician_positions = get_musician_positions(result['predictions'][0])
            execute_one_measure(MIDI_FILE_NAME, measure_number, musician_positions)
            time.sleep(2)
            
            # Check if any musician raised their hand to move to the next measure
            if any(is_hand_above_head(person['keypoints']) for person in result['predictions']):
                measure_number += 1  # Move to the next measure

        cv2.imshow('Camera Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Initialize the pose model
    model = init_pose_model()
    
    # Initialize the inferencer
    inferencer = MMPoseInferencer('wholebody')

    # Initialize the camera
    cap = cv2.VideoCapture('rtsp://192.168.100.88/1')

    # Ensure camera is ready
    if not cap.isOpened():
        print("Error: Couldn't open the camera.")
        exit()

    # Send camera to home position
    send_camera_control("home")
    time.sleep(4)

    # Load MIDI instructions
    instructions = robot_instructions(MIDI_FILE_NAME)

    # Process the video stream
    process_video_stream(cap, model, inferencer, instructions[0])



# Are we getting musician positions just once at the beginning and saving their positions, and referring back to them each time?
# Or are we iteratively updating positions?
# How to test functionality without having test subjects?