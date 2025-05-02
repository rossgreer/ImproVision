import time
import cv2
import numpy as np
from mmpose.apis import init_model, inference_topdown
from pythonosc.udp_client import SimpleUDPClient
import sys

### CONFIG ###
DEVICE = 'cuda'
CAMERA_IP = "192.168.100.88"  # camera IP
RTSP_STREAM = f'rtsp://{CAMERA_IP}/1'
MAC_IP = "[REPLACE WITH IP]"  # destination IP
PORT = 8000

HAND_RAISE_THRESHOLD = 50
HEAD_PROXIMITY_THRESHOLD = 125 # adjusted from 150
DETECTION_COOLDOWN = 5  # seconds after detecting a gesture

# Initialize OSC client
client = SimpleUDPClient(MAC_IP, PORT)

### POSE FUNCTIONS ###

def init_pose_model():
    model_cfg = '/home/cvrr/mmpose/configs/body_2d_keypoint/rtmpose/coco/rtmpose-m_8xb64-270e_coco-wholebody-256x192.py'
    ckpt = 'https://download.openmmlab.com/mmpose/v1/projects/rtmposev1/rtmpose-m_simcc-coco-wholebody_pt-aic-coco_270e-256x192-cd5e845c_20230123.pth'
    return init_model(model_cfg, ckpt, device=DEVICE)

def detect_gestures(keypoints):
    nose = keypoints[0]
    left_wrist = keypoints[9]
    right_wrist = keypoints[10]
    
    left_hand_raised = left_wrist[1] < nose[1] - HAND_RAISE_THRESHOLD
    right_hand_raised = right_wrist[1] < nose[1] - HAND_RAISE_THRESHOLD
    
    left_hand_to_head = np.linalg.norm(np.array(left_wrist[:2]) - np.array(nose[:2])) < HEAD_PROXIMITY_THRESHOLD
    right_hand_to_head = np.linalg.norm(np.array(right_wrist[:2]) - np.array(nose[:2])) < HEAD_PROXIMITY_THRESHOLD
    
    return (left_hand_raised or right_hand_raised), (left_hand_to_head or right_hand_to_head)

def detect_opposite_shoulder_touch(keypoints, threshold=50): # new
    left_wrist = keypoints[9]
    right_wrist = keypoints[10]
    left_shoulder = keypoints[5]
    right_shoulder = keypoints[6]

    left_wrist_to_right_shoulder = np.linalg.norm(np.array(left_wrist[:2]) - np.array(right_shoulder[:2]))
    right_wrist_to_left_shoulder = np.linalg.norm(np.array(right_wrist[:2]) - np.array(left_shoulder[:2]))

    touching = (left_wrist_to_right_shoulder < threshold) or (right_wrist_to_left_shoulder < threshold)
    return touching

def draw_keypoints(frame, keypoints, color=(0, 255, 0)):
    for i, keypoint in enumerate(keypoints):
        if len(keypoint) > 2 and keypoint[2] > 0.5:  # Confidence threshold
            cv2.circle(frame, (int(keypoint[0]), int(keypoint[1])), 3, color, -1)
            cv2.putText(frame, str(i), (int(keypoint[0]), int(keypoint[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        elif len(keypoint) == 2:
            cv2.circle(frame, (int(keypoint[0]), int(keypoint[1])), 3, color, -1)
            cv2.putText(frame, str(i), (int(keypoint[0]), int(keypoint[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

def main():
    model = init_pose_model()
    cap = cv2.VideoCapture(RTSP_STREAM)

    if not cap.isOpened():
        print("Error: Couldn't open the camera stream.")
        sys.exit(1)

    print("Starting gesture detection... Press 'q' to quit window.")

    start_time = time.time()
    last_detection_time = -DETECTION_COOLDOWN  # allow detection immediately

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame. Retrying...")
            time.sleep(1)
            continue

        current_time = time.time()

        if current_time - start_time < 3:
            # Skip detection for first few seconds
            cv2.imshow('Camera Stream', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            continue

        result = inference_topdown(model, frame)
        if len(result) > 0:
            for person in result:
                keypoints = person.pred_instances.keypoints[0]
                draw_keypoints(frame, keypoints)

                # Only detect gestures if enough time passed since last detection
                if current_time - last_detection_time >= DETECTION_COOLDOWN:
                    hand_raised, hand_to_head = detect_gestures(keypoints)
                    opposite_shoulder_touch = detect_opposite_shoulder_touch(keypoints) # new

                    if hand_raised and not hand_to_head:
                        print("Detected: Raised Hand")
                        client.send_message("/gesture", "raised-hand")
                        last_detection_time = current_time
                        filename = f"raised-hand_{time.strftime('%Y%m%d-%H%M%S')}.jpg"
                        cv2.imwrite(filename, frame)
                        print(f"Saved frame to {filename}")
                        last_detection_time = current_time
                    
                    elif hand_to_head and not hand_raised:
                        print("Detected: Hand to Head")
                        client.send_message("/gesture", "hand-to-head")
                        last_detection_time = current_time
                        filename = f"hand-to-head_{time.strftime('%Y%m%d-%H%M%S')}.jpg"
                        cv2.imwrite(filename, frame)
                        print(f"Saved frame to {filename}")
                        last_detection_time = current_time
                    
                    elif opposite_shoulder_touch: # new
                        print("Detected: Opposite Shoulder Touch")
                        client.send_message("/gesture", "opposite-shoulder-touch")
                        last_detection_time = current_time
                        filename = f"shoulder-touch_{time.strftime('%Y%m%d-%H%M%S')}.jpg"
                        cv2.imwrite(filename, frame)
                        print(f"Saved frame to {filename}")
                        last_detection_time = current_time

        cv2.imshow('Camera Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
