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

# def send_camera_control(command):
#     """
#     Sends a command to the camera and checks the response status. 
#     """
#     url = CAMERA_URL + command
#     response = requests.get(url)
#     if response.status_code == 200:
#         print(f"Command '{command}' was successful")
#     else:
#         print(f"Failed to execute command '{command}'")

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
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Command '{url}' was successful")
        return "success"
    else:
        print(f"Failed to execute command '{url}'")
        return "failure"

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

def execute_one_measure(midi_file_name, measure_number, musician_positions): # currently unused, this is the more complex thing
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

def time_for_turn_by_proportion_of_range(target_nose_x): # also currently unused
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

def is_hand_above_head(person_landmarks): # check later, currently unused
    """
    Checks if any hand is raised above the head.
    """
    nose_y = person_landmarks['nose'][1]
    left_wrist_y = person_landmarks['left_wrist'][1]
    right_wrist_y = person_landmarks['right_wrist'][1]
    return left_wrist_y < nose_y or right_wrist_y < nose_y

def get_musician_positions(results): # check later too
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

def simple_execute_one_measure(midi_file_name, measure_number): # just for now, use actual positions later
    instructions_by_measure = robot_instructions(midi_file_name)

    if measure_number < 1 or measure_number > len(instructions_by_measure):
        print(f"Measure number {measure_number} is out of range for the given MIDI file.")
        return

    measure_instructions = instructions_by_measure[measure_number - 1]

    # Center
    send_camera_control("home")
    time.sleep(4)

    ### REPLACE: find person on far left ###
    # Start by panning to the far left
    send_camera_control("left")  
    time.sleep(1.5)  # Wait a bit
    send_camera_control("ptzstop")  # Stop the camera movement

    # Iterate over instruments in order
    for instrument in INSTRUMENT_ORDER:
        time.sleep(1)
        movement = measure_instructions.get(instrument)
        if movement:
            print(f"Executing movement for {instrument}: {movement}")
            execute_movement_for_instrument(movement) # See helper function below
        else:
            print(f"{instrument} has no specific movement. 'Looking' at the instrument.")
            time.sleep(1)
        
        time.sleep(1)

        # Pan to the next instrument on the right
        if instrument != INSTRUMENT_ORDER[-1]:
            ### REPLACE: find next person towards the right ###
            send_camera_control("right")
            time.sleep(1)  
            send_camera_control("ptzstop")
    
    # Final 'slam' cue
    send_camera_control("home")
    time.sleep(3)
    send_camera_control('ptzstop')
    time.sleep(1)
    send_camera_control('up')
    time.sleep(0.7)
    send_camera_control('down')
    time.sleep(0.7)

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
        time.sleep(2)
        send_camera_control("down")
        time.sleep(0.6)
        send_camera_control("ptzstop")
    elif movement == "up whole":
        send_camera_control("up")
        time.sleep(0.5)
        send_camera_control("ptzstop")
        time.sleep(0.5)  # Pause between half steps
        send_camera_control("up")
        time.sleep(0.5)
        send_camera_control("ptzstop")
        # Return to horizontal
        time.sleep(2)
        send_camera_control("down")
        time.sleep(0.6)
        send_camera_control("ptzstop")
    elif movement == "down half":
        send_camera_control("down")
        time.sleep(0.7)
        send_camera_control("ptzstop")
        # Return to horizontal
        time.sleep(2)
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
        time.sleep(2)
        send_camera_control("up")
        time.sleep(0.7)
        send_camera_control("ptzstop")

def process_video_stream(cap, model, instructions):
    """
    Processes the video stream to detect hand-raising gestures and execute movements.
    """
    measure_number = 1  # Initialize measure number
    time.sleep(.5) 

    # to avoid detection of same raised hand in multiple consecutive frames, add debounce mechanism
    debounce_time = 3
    last_detection_time = time.time()

    i = 0
    while True:
        i += 1
        ret, frame = cap.read()

        # Set the desired frame rate (e.g., 2 frames per second)
        desired_fps = 1
        delay = int(1000 / desired_fps)

        if not ret:
            print("Failed to read frame from camera.")
            print("Attempting Camera Stream restart.")
            #break
            #continue
            cap.release()
            cv2.destroyAllWindows()
            # Initialize the camera
            while not cap.isOpened():
                cap = cv2.VideoCapture('rtsp://192.168.100.88/1')

                # Ensure camera is ready
                if not cap.isOpened():
                    print("Error: Couldn't open the camera.")
                    print("Attempting restart.")
                    #exit()
                else:
                    ret, frame = cap.read()

        print("Frame read successfully "+str(i))

        result = inference_topdown(model, frame)
        #print(f"Raw inference result: {result}")
        #print(type(result))
        #for person in result: # each thing in result is one detected person
            #print("THIS IS ONE ITEM")
            #print(thing)

        hand_raised_detected = False

        #if len(result) > 0 and 'predictions' in result[0]:
        if len(result) > 0 and (time.time() - last_detection_time > debounce_time): # and 'predictions' in result:

            for person in result:
                keypoints = person.pred_instances.keypoints[0] # keypoints for one person
                print("Detected keypoints:")
                print(keypoints)
                print(len(keypoints))

                # https://mmpose.readthedocs.io/en/latest/dataset_zoo/2d_wholebody_keypoint.html#coco-wholebody 
                nose = keypoints[0] 
                left_arm = keypoints[10]
                right_arm = keypoints[11]

                print(f"Nose position: {nose}")
                print(f"Left arm position: {left_arm}")
                print(f"Right arm position: {right_arm}")

                # Check if either arm is above the nose by comparing y coordinates. Assuming y increases towards bottom of frame.
                if left_arm[1] < nose[1] or right_arm[1] < nose[1]:
                    print("Hand raised detected!")
                    hand_raised_detected = True
                    last_detection_time = time.time()
                    break # break out if raised hand is detected

            # if hand_raised_detected:
            #     measure_number += 1
            #     print(f"Moving on to measure number: {measure_number}")
            #     execute_one_measure(MIDI_FILE_NAME, measure_number, )
            #     if measure_number > len(instructions):
            #         print("All measures completed.")
            #         break

            #p1 = result[0]
            # print(type(p1))
            # print(p1)
            # print("Keypoints")
            # print(p1.pred_instances)
            # print("did that work")
            #print(p1.pred_instances.keypoints) # gives pixel locations of detected keypoints
            #print("let's go")
            #print(p1['keypoints'])
            # ['predictions']
            # p2 = p1[0]
            # p3 = p2[0]
            # p4 = p3['keypoints']
            
            #person_nose = result['predictions'][0][0]['keypoints'][0]
            #check = result['predictions'][0][0]['bbox'][0][0]

            #if not check - 0 < 0.5:
                #print("Person Found")
                #print(person_nose)
        
            # musician_positions = get_musician_positions(result[0]['predictions'])
            # print(f"Musician positions: {musician_positions}")

            # execute_one_measure(MIDI_FILE_NAME, measure_number, musician_positions)
            # print(f"Executed measure number: {measure_number}")
            # time.sleep(2)
            
            # # Check if any musician raised their hand to move to the next measure
            # if any(is_hand_above_head(person['keypoints']) for person in result['predictions']):
            #     measure_number += 1  # Move to the next measure
            #     print(f"Moving on to measure number: {measure_number}")
            #     if measure_number > len(instructions):
            #         print("All measures completed.")
            #         break

        else:
            print("No valid predictions found in the frame.")

        if hand_raised_detected:
            measure_number += 1
            print(f"Moving on to measure number: {measure_number}")

            # Pause detection and execute the next measure
            simple_execute_one_measure(MIDI_FILE_NAME, measure_number)
            
            if measure_number > len(instructions):
                print("All measures completed.")
                break

        # Wait for a specific amount of time (in milliseconds)

        if i % 20 == 0:
            cv2.imshow('Camera Stream', frame)
            # Exit the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        #time.sleep(1)

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Initialize the pose model
    model = init_pose_model()
    
    # Initialize the inferencer
    #inferencer = MMPoseInferencer('wholebody')

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
    print(f"Loaded instructions: {instructions}")

    # Process the video stream
    process_video_stream(cap, model, instructions)

