import numpy as np
import cv2

image = cv2.imread('D:/Image/ara.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('bird', image)

cv2.waitKey(0)

cv2.destroyAllWindow()
