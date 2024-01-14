from ultralytics import YOLO

model = YOLO("yolov8n.yaml")  # build a new model from scratch

results = model.train(data="config.yaml", epochs=150, patience=80, resume=True)  # train the model
