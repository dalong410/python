# 실습 : 이미지 확대 & 축소하기

import cv2

src = cv2.imread("d:/py/Image/fruits.jpg", cv2.IMREAD_COLOR)

height, width, channel = src.shape

# cv2.pyrUp 이미지 확대 
dst = cv2.pyrUp(src, dstsize=(width*2, height*2), borderType=cv2.BORDER_DEFAULT);

# 이미지 축소하기 -> 기본값 1/2
dst2 = cv2.pyrDown(src);

cv2.imshow("src", src)

cv2.imshow("dst", dst)

cv2.imshow("dst2", dst2)

cv2.waitKey(0)

cv2.destroyAllWindows()
