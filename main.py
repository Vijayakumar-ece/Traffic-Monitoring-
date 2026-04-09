import cv2
import torch
import ultralytics.nn.tasks as tasks
from ultralytics import YOLO

# Fix for torch 2.6
torch.serialization.add_safe_globals([tasks.DetectionModel])

# Delete old model file and re-download
import os
model_path = 'yolov8n.pt'
if os.path.exists(model_path):
    os.remove(model_path)
    print("Old model deleted!")

# Model load
model = YOLO('yolov8n.pt')
print("Model loaded!")

video_path = r'C:\traffic_system\videos\traffic.mp4'
cap = cv2.VideoCapture(video_path)

print("Video opened:", cap.isOpened())
print("Starting... Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Video ended!")
        break

    results = model.predict(source=frame, conf=0.3, verbose=False)
    annotated = results[0].plot()
    annotated = cv2.resize(annotated, (900, 500))

    cv2.namedWindow('Traffic Detection', cv2.WINDOW_NORMAL)
    cv2.imshow('Traffic Detection', annotated)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Done!")
