# import serial
# import serial.rs485
import requests
import time
import cv2
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# !pip install -q mediapipe
# !wget -O pose_landmarker.task -q https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_heavy/float16/1/pose_landmarker_heavy.task
# https://community.ptzoptics.com/s/article/How-do-I-get-the-PTZOptics-camera-up-on-my-network-Quick-Setup

#https://ptzoptics.com/networking-help-setting-up-a-ptz-camera-on-your-network/

# Note: made network IP 192.168.100.90, gateway 192.168.100.1, netmask 255.255.255.0
# Camera IP is 192.168.100.88


# URL of the camera stream
#camera_url = "http://192.168.100.88/video"


def draw_landmarks_on_image(rgb_image, detection_result):
  pose_landmarks_list = detection_result.pose_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected poses to visualize.
  for idx in range(len(pose_landmarks_list)):
    pose_landmarks = pose_landmarks_list[idx]

    # Draw the pose landmarks.
    pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    pose_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      pose_landmarks_proto,
      solutions.pose.POSE_CONNECTIONS,
      solutions.drawing_styles.get_default_pose_landmarks_style())
  return annotated_image


def sample_image(img):
    # STEP 2: Create an PoseLandmarker object.
    base_options = python.BaseOptions(model_asset_path='pose_landmarker.task')
    options = vision.PoseLandmarkerOptions(
        base_options=base_options,
        output_segmentation_masks=True)
    detector = vision.PoseLandmarker.create_from_options(options)

    # STEP 4: Detect pose landmarks from the input image.
    detection_result = detector.detect(img)

    # STEP 5: Process the detection result. In this case, visualize it.
    annotated_image = draw_landmarks_on_image(img.numpy_view(), detection_result)
    return cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)


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

# post("up")
# time.sleep(1)
# post("down")
# time.sleep(1)
# post("ptzstop")

# post("home")
# time.sleep(2)
# post("left")
# time.sleep(1)
# post("ptzstop")

if __name__ == "main":
    # Create a VideoCapture object
    cap = cv2.VideoCapture('rtsp://192.168.100.88/1')

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Couldn't open the camera.")
        exit()

    # Loop to continuously capture frames
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly, display it
        if ret:
            pose_image = sample_image(frame)
            cv2.imshow('Camera Stream', pose_image)

        # Check for 'q' key pressed to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object and close all windows
    cap.release()
    cv2.destroyAllWindows()
