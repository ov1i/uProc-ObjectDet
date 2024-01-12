from ultralytics import YOLO

model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="config.yaml", epochs=1, resume=True)  # train the model
