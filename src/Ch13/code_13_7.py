import numpy as np
import cv2

image = cv2.imread('d:/data/mandrill.png')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

blue_low = np.array([80, 0, 0])
blue_high = np.array([130, 255, 255])

mask = cv2.inRange(image_hsv, blue_low, blue_high)

cv2.imshow('original', image)
cv2.imshow('mask', mask)

extracted = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('extracted', extracted)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
