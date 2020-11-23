import numpy as np
import cv2

original_image = cv2.imread('d:/data/mandrill.png', 1)
result_image1 = cv2.GaussianBlur(original_image,  (9,9), 1)
result_image2 = cv2.medianBlur(original_image, 9)
result_image3 = cv2.bilateralFilter(original_image, 9, 50, 50)

cv2.imshow('original', original_image)
cv2.imshow('Gauss', result_image1)
cv2.imshow('bilateralFilter', result_image2)
cv2.imshow('medianBlur', result_image3)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
