# yolo를 이용한 인식(검출)
import numpy as np
import cv2 as cv
import sys

from picamera2 import Picamera2
from ultralytics import YOLO
import matplotlib.pyplot as plt

# # Load a YOLO11n PyTorch model
# model = YOLO("yolo11n.pt")

# # Export the model to NCNN format
# model.export(format="ncnn")  # creates 'yolo11n_ncnn_model'

# Load the exported NCNN model
ncnn_model = YOLO("yolo11n_ncnn_model/")

picam2 = Picamera2()
picam2.configure(
    picam2.create_video_configuration(
        main={"size": (640, 480)}, controls={"FrameDurationLimits": (100000, 100000)}
    )
)
picam2.configure("video")
picam2.start()

# 영상 라즈베리 캠영상에 yolo_v3 적용
# cap = cv.VideoCapture("http://192.168.0.121:8000/stream.mjpg")
# if not cap.isOpened():
#     sys.exit("카메라 영상 연결 실패")

while True:
    frame = picam2.capture_array()
    # if not ret:
    #     sys.exit("프레임 획득에 실패했습니다. 루프에서 나갑니다.")

    result = ncnn_model(cv.flip(frame, 0))

    cv.imshow("Object detection by YOLO11n-ncnn ", result[0].plot())

    key = cv.waitKey(1)
    if key == ord("q"):
        break

# cap.release()  # 카메라 연결 종료
cv.destroyAllWindows()
