import cv2
import time
import json
import os
from detect_objects import detect_objects

video_path = r"C:\Users\MSI\Desktop\Surya New\Safetywhat\test_video.mp4" 


if not os.path.exists(video_path):
    print(f"Error: Video file not found at {video_path}")
    exit()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

output_json = 'output.json'
detections = []

start_time = time.time()

frame_count = 0
while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    detected_objects = detect_objects(frame)

    
    for obj in detected_objects:
        obj['id'] = int(obj['id'])  
        obj['bbox'] = [int(coord) for coord in obj['bbox']]  


    detections.extend(detected_objects)

    
    frame_count += 1


end_time = time.time()
elapsed_time = end_time - start_time
fps = frame_count / elapsed_time

with open(output_json, 'w') as f:
    json.dump(detections, f, indent=4)


print(f"Frames processed: {frame_count}")
print(f"Total time taken: {elapsed_time:.2f} seconds")
print(f"Inference FPS: {fps:.2f}")


cap.release()

print("Object detection completed. Output saved in output.json.")
