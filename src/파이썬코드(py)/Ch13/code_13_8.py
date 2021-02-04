#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 13.8 이미지에 필터를 씌워 보자, 350쪽
#
import numpy as np
import cv2

org = cv2.imread('d:/data/mandrill.png', 1)

kernel1 = np.ones((3, 3), np.float32) / 9
kernel2 = np.ones((9, 9), np.float32) / 81

averaged33 = cv2.filter2D(org, -1, kernel1)
averaged99 = cv2.filter2D(org, -1, kernel2)

cv2.imshow('original', org)
cv2.imshow('filtered1', averaged33)
cv2.imshow('filtered2', averaged99)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()