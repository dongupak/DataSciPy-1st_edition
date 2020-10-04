import cv2

img_gray = cv2.imread('d:/data/mandrill.png', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('d:/data/mandrill.png', cv2.IMREAD_COLOR)

cv2.imshow('grayscale', img_gray)    # 맨드릴 원숭이를 회색조 이미지로 화면에 표시
cv2.imshow('color image', img_color) # 맨드릴 원숭이를 컬러 이미지로 화면에 표시

#cv2.waitKey(0)
