import numpy as np
import cv2

image = cv2.imread("d:\python\Image/moon.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow('MOON', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
