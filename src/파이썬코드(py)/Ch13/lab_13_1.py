#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 13-1 합성 사진 만들기 2, 359쪽
#
import numpy as np
import cv2

img1 = cv2.imread('d:/data/green_back.png')       # 전경 이미지 읽기
img2 = cv2.imread('d:/data/iceberg.png')          # 배경 이미지 읽기

front_image = cv2.resize(img1, (300, 400))
back_image = cv2.resize(img2, (300, 400))

img_hsv = cv2.cvtColor(front_image, cv2.COLOR_BGR2HSV)   # HSV 공간으로 옮김
l_bound = np.array([40, 100, 50])                 # 녹색 색상의 하한
u_bound = np.array([80, 255, 255])                # 녹색 색상의 상한

my_mask  = cv2.inRange(img_hsv, l_bound, u_bound)   # 녹색 픽셀 찾기
mask_inv = cv2.bitwise_not(my_mask)                 # 녹색이 아닌 픽셀 찾기

# 녹색 픽셀들만 추출하기
extracted = cv2.bitwise_and(front_image, front_image, mask = my_mask) 
# 녹색 아닌 픽셀만 추출하기
removed = cv2.bitwise_and(front_image, front_image, mask = mask_inv)   
# 녹색과 겹치는 배경 추출
background = cv2.bitwise_and(back_image, back_image, mask = my_mask)   
# 녹색 제거 전경 + 배경   
merged = cv2.bitwise_or(removed, background)
             
cv2.imshow('mask', my_mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('removed', removed)
cv2.imshow('background', background)
cv2.imshow('merged', merged)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드로 향후 코드에서는 생략함
cv2.waitKey(0)                       # 사용자 입력을 기다림
cv2.destroyAllWindows()              # 모든 창을 없애고 프로그램 종료