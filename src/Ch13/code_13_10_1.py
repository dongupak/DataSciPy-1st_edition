import numpy as np
import cv2

original_image = cv2.imread('d:/data/salt_pepper.png', 0)
result_image = cv2.medianBlur(original_image,  5)

cv2.imshow('original', original_image)
cv2.imshow('medianBlur', result_image)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
