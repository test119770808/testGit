## 라즈베리파이 에서 실행 코드
import cv2
import numpy as np
import sys

# connstr은 libcamera의 정보를 사용하여 접근하기 위한 값.
connstr = 'libcamerasrc ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert ! videoscale ! clockoverlay time-format="%D %H:%M:%S" ! appsink'
# connstr 정보를 가지고 , CAP_GSTREAMER 를 사용한 비디오캡쳐 기능...
#                      CAP_GSTREAMER 사용하기 위해서 컴파일 시 설정 필요(cv2.getBuildInformation()에서 확인)
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print("camera open Failed")
    sys.exit(0)

while True:
    succes, img = (
        cap.read()
    )  # success 데이터 로드 성공여부(성공시 True, 실패시 False), img에 데이터 존재함
    if succes == False:
        print("camera read Failed")
        sys.exit(0)

    k = cv2.waitKey(1)  # waitKey() 키보드 입력 대기...  단위 ms
    if k == ord("q"):
        break

    cv2.imshow("Img", img)  # 카메라 이미지를 보여줌

cap.release()  # 카메라 연결 해제
cv2.destroyAllWindows()
