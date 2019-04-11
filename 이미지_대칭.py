# 실습 : 대칭이미지 만들기

import cv2

# 사용할 이미지 불러오기
src = cv2.imread("d:py:Image/glass.jpg", cv2.IMREAD_COLOR)

# 이미지 작업 결과 적용 & 대칭 함수 선언, 0은 상하대칭, 1은 좌우대칭
dst = cv2.flip(src, 0)

# 원본 이미지 출력
cv2.imshow("src", src)

# 작업 이미지 출력
cv2.imshow("dst", dst)

# 지정된 키값이 0일 경우 다음으로 넘어가지 않고 현재 작업을 계속 유지한다.
cv2.waitKey(0)

# 작업 종료시 창을 닫는다
cv2.destroyAllWindows()
