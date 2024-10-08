# import serial
# import serial.rs485
import requests
import time
import cv2
#from mediapipe import solutions
#from mediapipe.framework.formats import landmark_pb2
import numpy as np
# import mediapipe as mp
# from mediapipe.tasks import python
# from mediapipe.tasks.python import vision
import matplotlib.pyplot as plt
from mmpose.apis import MMPoseInferencer

#from mmpose import infer, vis

# https://mmcv.readthedocs.io/en/latest/get_started/build.html

# Load pre-trained pose estimation model
pose_model = infer.init_pose_model(config='hrnet_pose.py',
                                   checkpoint='hrnet_w32_256x192.pth',
                                   device='cuda')

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # instantiate the inferencer using the model alias
    inferencer = MMPoseInferencer('human')

    # The MMPoseInferencer API employs a lazy inference approach,
    # creating a prediction generator when given input
    result_generator = inferencer(frame, show=True)
    result = next(result_generator)
    print("Next")

    # # Perform pose estimation
    # pose_results, _ = infer.inference_top_down_pose_model(
    #     pose_model, frame)

    # # Visualize pose estimation results
    # vis.show_multi_pose_result(frame, pose_results, show=False)

    # # Display the result
    # cv2.imshow('Pose Estimation', frame)

    # # Exit when 'q' is pressed
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()


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

# previous sample_image function
# def sample_image(img):
#     # STEP 2: Create an PoseLandmarker object.
#     base_options = python.BaseOptions(model_asset_path='pose_landmarker_lite.task')
#     options = vision.PoseLandmarkerOptions(
#         base_options=base_options,
#         output_segmentation_masks=True, num_poses = 8)
#     detector = vision.PoseLandmarker.create_from_options(options)

#     rgb_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=img)

#     # STEP 4: Detect pose landmarks from the input image.
#     detection_result = detector.detect(rgb_frame)
#     print(detection_result)

#     # STEP 5: Process the detection result. In this case, visualize it.
#     annotated_image = draw_landmarks_on_image(rgb_frame.numpy_view(), detection_result)

#     return annotated_image
#     #return cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)

def sample_image(img):
    base_options = python.BaseOptions(model_asset_path='pose_landmarker_lite.task')
    options = vision.PoseLandmarkerOptions(
        base_options=base_options,
        output_segmentation_masks=True)
    detector = vision.PoseLandmarker.create_from_options(options)

    rgb_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=img)

    detection_result = detector.detect(rgb_frame)

    annotated_image = draw_landmarks_on_image(rgb_frame.numpy_view(), detection_result)

    # Want to return wrist and nose landmarks
    if detection_result.pose_landmarks:
        extracted_landmarks = {}
        for landmark in detection_result.pose_landmarks:
            if landmark.HasField('landmark'):
                extracted_landmarks = {
                    'nose': landmark.landmark[0],  # Nose landmark
                    'left_wrist': landmark.landmark[15],  # Left wrist landmark
                    'right_wrist': landmark.landmark[16]  # Right wrist landmark
                }
                break  # Currently assuming single-person detection, break after the first set of landmarks -- change later

        return annotated_image, extracted_landmarks
    else:
        return annotated_image, {}



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

#if __name__ == "main":


# Loop to continuously capture frames
while True:
    # Capture frame-by-frame
    cap = cv2.VideoCapture('rtsp://192.168.100.88/1')

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Couldn't open the camera.")
        exit()

    ret, frame = cap.read()

    # If frame is read correctly, display it
    if ret:
        pose_image, landmarks = sample_image(frame)
        if landmarks:
            # Detect if either wrist is raised above the nose
            # Comparing the y-coordinates because the origin is at the top left corner
            if landmarks['left_wrist'].y < landmarks['nose'].y or landmarks['right_wrist'].y < landmarks['nose'].y:
                print("Arm is raised")
        cv2.imshow('Camera Stream', pose_image)
    # Check for 'q' key pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()