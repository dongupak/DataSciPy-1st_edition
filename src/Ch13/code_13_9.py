#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 13.9 OpenCV로 이미지 필터링하기, 352쪽
#
import numpy as np
import cv2

org = cv2.imread('d:/data/mandrill.png', 1)

averaged33 = cv2.GaussianBlur(org, (3,3), 1)
averaged99 = cv2.GaussianBlur(org, (9,9), 1)

cv2.imshow('original', org)
cv2.imshow('Gaussian 33', averaged33)
cv2.imshow('Gaussian 99', averaged99)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()