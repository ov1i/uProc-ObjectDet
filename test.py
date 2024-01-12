import os.path

import cv2
from ultralytics import YOLO

img = cv2.imread("test.jpg")

model_path = os.path.join('.', 'runs', 'detect', 'train7', 'weights', 'best.pt')

model = YOLO(model_path)

threshold = 0.5


results = model(img)[0]

for res in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = res
    cv2.rectangle(img, (int(x1), int(y1), int(x2), int(y2)), (255, 0, 0), 4)
    cv2.putText(img, results.names[int(class_id)].upper(), (int(x1), int(y1-10)), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
    

cv2.imwrite("res.jpg", img)
cv2.imshow("Test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
