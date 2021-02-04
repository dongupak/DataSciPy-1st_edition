#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 13.3 좀 더 편리한 이미지 도구는 없을까, 343쪽
#
import cv2

img_gray = cv2.imread('d:/data/mandrill.png', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('d:/data/mandrill.png', cv2.IMREAD_COLOR)

cv2.imshow('grayscale', img_gray)    # 맨드릴 원숭이를 회색조 이미지로 화면에 표시
cv2.imshow('color image', img_color) # 맨드릴 원숭이를 컬러 이미지로 화면에 표시

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()