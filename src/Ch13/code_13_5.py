#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 13.5 합성 사진을 제작해 보자, 345쪽
#
import cv2

global img1, img2     # 두 이미지를 프로그램의 전체에서 사용할 수 있도록 함

def on_change_weight(x):   # 트랙바가 움직이게 되면 이 함수가 호출된다
    weight = x / 100       # x 값이 0에서 100사이이므로 100으로 나누어 0에서 1사이 값으로
    img_merged = cv2.addWeighted(img1, 1-weight, img2, weight, 0)
    cv2.imshow('Display', img_merged)

cv2.namedWindow('Display')
cv2.createTrackbar('weight', 'Display', 0, 100, on_change_weight)

img1 = cv2.imread('d:/data/green_back.png')
img2 = cv2.imread('d:/data/iceberg.png')
img1 = cv2.resize(img1, (300,400))
img2 = cv2.resize(img2, (300,400))

cv2.imshow('Display', img1)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()