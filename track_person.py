import cv2
import numpy as np
#from mmpose.apis import inference_top_down_pose_model, init_pose_model, vis_pose_result
import requests
import time
import matplotlib.pyplot as plt
from mmpose.apis import MMPoseInferencer

from mmcv.image import imread

from mmpose.apis import inference_topdown, init_model
from mmpose.registry import VISUALIZERS
from mmpose.structures import merge_data_samples




# Adjust these parts depending on how we structure the directory
# config_file = 'path/to/mmpose/config/crowdpose.py'  
# checkpoint_file = 'path/to/checkpoint/crowdpose.pth'  
# device = 'cuda:0'  
# pose_model = init_pose_model(config_file, checkpoint_file, device=device)

# MMPose has its own visualization function, see vis_pose_result in sample_img function below
# So draw_landmarks_on_image function has been removed

# Keypoint index mapping: https://github.com/open-mmlab/mmpose/blob/main/configs/_base_/datasets/coco.py

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
            'nose': keypoints[0], #[12],  
            'left_wrist': keypoints[9], #[4],
            'right_wrist': keypoints[10]
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


#def initialize_musicians():
    # Approach 1:
    # Keep track of the musician locations from 'home' position
    # Count how many musicians you should pass before beginning to hone in on the target
    # Should only move in one direction; stop when the target is left-of-center

    # Approach 2: 
    # Form angle estimate of each musician (or cluster)
    # Form motor estimate to reach this angle




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


def time_for_turn_by_proportion_of_range(target_nose_x):
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
        target_motion_time = (1920/2-target_nose_x) / rate_left


    return target_motion_time, direction


if __name__ == "__main__":
    # instantiate the inferencer using the model alias
    post('home')
    time.sleep(4)
    #inferencer = MMPoseInferencer('wholebody')
    model_cfg = '/home/cvrr/mmpose/configs/body_2d_keypoint/rtmpose/coco/rtmpose-m_8xb64-270e_coco-wholebody-256x192.py' # 


    ckpt = 'https://download.openmmlab.com/mmpose/v1/projects/rtmposev1/rtmpose-m_simcc-coco-wholebody_pt-aic-coco_270e-256x192-cd5e845c_20230123.pth'

    device = 'cuda'

    # init model
    model = init_model(model_cfg, ckpt, device=device)


    cap = cv2.VideoCapture('rtsp://192.168.100.88/1')


    #musician_positions = initialize_musicians()
    i = 0

    while True:
        print("Entered loop")


        if not cap.isOpened():
            print("Error: Couldn't open the camera.")
            break  # Exit the loop if camera can't be accessed

        ret, frame = cap.read()
       
        if ret:

            result = inference_topdown(model, frame)
            #cv2.imwrite("im_"+str(i)+".jpg", frame)
            # result_generator = inferencer(frame, show=False)
            # result = next(result_generator)
            #print(result['predictions'])

            person_nose = result['predictions'][0][0]['keypoints'][0]
            check = result['predictions'][0][0]['bbox'][0][0]

            if not check - 0 < 0.5:
                print("Person Found")
                print(person_nose)

                person_nose_x = person_nose[0]


                if person_nose_x > 1920/2:
                    post("right")
                    time.sleep(0.1)
                    post("ptzstop")
                else:
                    post("left")
                    time.sleep(0.1)
                    post("ptzstop")
        


            # turn_time, turn_dir = time_for_turn_by_proportion_of_range(person_nose[0])

            # post(turn_dir)
            # time.sleep(turn_time)
            # post('ptzstop')


            # post("up")
            # time.sleep(0.5)
            # post("ptzstop")
            # time.sleep(0.5)  # Pause between half steps
            # post("up")
            # time.sleep(0.5)
            # post("ptzstop")
            # # Return to horizontal
            # time.sleep(2)
            # post("down")
            # time.sleep(0.6)
            # post("ptzstop")

            # # time.sleep(5)
            # # post('home')
            # # time.sleep(4)




            # # Final 'slam' cue
            # post("home")
            # time.sleep(3)
            # post('ptzstop')
            # time.sleep(1)
            # post('up')
            # time.sleep(0.7)
            # post('down')
            # time.sleep(0.7)

            # time.sleep(1)
            # # Center
            # post("home")
            # time.sleep(4)

            # pose_image, all_extracted_landmarks = sample_image(frame)
            
            # # Check each person for hand-above-head gesture
            # for person_landmarks in all_extracted_landmarks:
            #     if is_hand_above_head(person_landmarks):
            #         print("Detected a person with their hand above their head.")

            # # Display video stream with pose estimation
            # cv2.imshow('Camera Stream', pose_image)

        #time.sleep(.25)
        
        # Check for 'q' key to exit loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #break
        i += 1
    cap.release()
    cv2.destroyAllWindows()
