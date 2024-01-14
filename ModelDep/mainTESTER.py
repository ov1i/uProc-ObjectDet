from ultralytics import YOLO
import os

model_path = os.path.join("..", "runs", "detect", "train8", "weights", "best.pt")

model = YOLO(model_path)

frame_path = "0"
results = model.predict(source=frame_path, show=True)

print(results)
