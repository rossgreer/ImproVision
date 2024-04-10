import cv2
import numpy as np
from mmpose.apis import inference_top_down_pose_model, init_pose_model, vis_pose_result
import requests
import time
import matplotlib.pyplot as plt

# Adjust these parts depending on how we structure the directory
config_file = 'path/to/mmpose/config/crowdpose.py'  
checkpoint_file = 'path/to/checkpoint/crowdpose.pth'  
device = 'cuda:0'  
pose_model = init_pose_model(config_file, checkpoint_file, device=device)

# MMPose has its own visualization function, see vis_pose_result in sample_img function below
# So draw_landmarks_on_image function has been removed

def sample_image(img):
    # Pose estimation
    pose_results, _ = inference_top_down_pose_model(
        pose_model,
        img,
        person_results=None, 
        bbox_thr=None,
        format='xyxy',
        dataset='TopDownCrowdPoseDataset')
    
    # Visualization
    vis_img = vis_pose_result(
        pose_model,
        img,
        pose_results,
        dataset='TopDownCrowdPoseDataset',
        kpt_score_thr=0.3,
        radius=4,
        thickness=4,
        show=False)

    # Extract landmarks, separately for each person
    # Landmark numbers for CrowdPose from https://mmpose.readthedocs.io/en/latest/dataset_zoo/2d_body_keypoint.html#crowdpose
    all_extracted_landmarks = []
    for person_pose in pose_results:
        keypoints = person_pose['keypoints']
        person_landmarks = {
            'nose': keypoints[12],  
            'left_wrist': keypoints[4],
            'right_wrist': keypoints[5]
        }
        all_extracted_landmarks.append(person_landmarks)

    return vis_img, all_extracted_landmarks

def is_hand_above_head(person_landmarks):
    nose_y = person_landmarks['nose'][1]  # Assuming [x, y, (z)] format
    left_wrist_y = person_landmarks['left_wrist'][1]
    right_wrist_y = person_landmarks['right_wrist'][1]
    return left_wrist_y < nose_y or right_wrist_y < nose_y


def sendCameraControl(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print("Command: " + url + " was successful")
        return "success"
    else:
        print("An Error occured while ")
        return "success"

# buildUrl will create the HTTP CGI commands using the data passed to it.
# Once finished it will return the processed url to the function that called it.
def buildCgiUrl(command):
    url = 'http://' + "192.168.100.88" + '/cgi-bin/ptzctrl.cgi?ptzcmd&'
    action = command #"up" #req["param[action]"]
    panSpeed = str(24)
    tiltSpeed = str(20)

    # All vector motion actions
    if action == "up" or action == "down" or action == "left" or action =="right":
        # panSpeed = req["param[panSpeed]"]
        # tiltSpeed = req["param[tiltSpeed]"]
        return url + action + '&' + panSpeed + '&' + tiltSpeed
    # All non-directional motion actions
    elif action == "home" or action == "ptzstop":
        return url + action
    # All Focus actions
    elif action == "focusin" or action == "focusout" or action == 'focusstop':
        focusSpeed = req["param[focusSpeed]"]
        return url + action + '&' + focusSpeed
    # All Zoom actions
    elif action == "zoomin" or action == "zoomout" or action == 'zoomstop':
        zoomSpeed = req["param[zoomSpeed]"]
        return url + action + '&' + zoomSpeed
    else:
        return url + 'home' + '&10&10';

# pan speed goes up to 24
# tilt speed goes up to 20

def post(command):
    return sendCameraControl(buildCgiUrl(command))

while True:
    cap = cv2.VideoCapture('rtsp://192.168.100.88/1')

    if not cap.isOpened():
        print("Error: Couldn't open the camera.")
        break  # Exit the loop if camera can't be accessed

    ret, frame = cap.read()

    if ret:
        pose_image, all_extracted_landmarks = sample_image(frame)
        
        # Check each person for hand-above-head gesture
        for person_landmarks in all_extracted_landmarks:
            if is_hand_above_head(person_landmarks):
                print("Detected a person with their hand above their head.")

        # Display video stream with pose estimation
        cv2.imshow('Camera Stream', pose_image)
    
    # Check for 'q' key to exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()