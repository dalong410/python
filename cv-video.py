import numpy as np
import cv2
capture = cv2.VideoCapture("d:/py/Image/NutJob2.mp4")

while True :
	if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
		capture.open("d:/py/Image/NutJob2.mp4")

	ret, frame = capture.read()
	cv2.imshow("VideoFrame", frame)

	if cv2.waitKey(33) > 0 : break

capture.release()
cv2.destroyAllWindows()
