# 실습 : 카메라 사용하기

import cv2

# 노트북의 경우 내장카메라(0번을 부여), 외장카메라(1 ~ N값을 부여받는다)
capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    if cv2.waitKey(1) > 0: break

# 아무키나 입력할 경우 종료한다.
# q키를 입력하면 종료하기 구문 작성
#if cv2.waitKey(1)==ord('q'): break

# 카메라에서 받아온 영상의 메모리를 해제한다.
capture.release()
# 창을 닫는다.
cv2.destroyAllWindows()
