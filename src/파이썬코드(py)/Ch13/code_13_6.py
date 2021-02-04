#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 13.6 이미지에 마스크를 씌워볼까, 346쪽
#
import cv2
mask_image = cv2.imread('d:/data/mask_circle.png')
back_image = cv2.imread('d:/data/iceberg.png')
mask_image = cv2.resize(mask_image, (300,400))
back_image = cv2.resize(back_image, (300,400))

mask_ANDed = cv2.bitwise_and(mask_image, back_image)
mask_ORed = cv2.bitwise_or(mask_image, back_image)
mask_XORed = cv2.bitwise_xor(mask_image, back_image)

cv2.imshow('mask', mask_image)
cv2.imshow('back', back_image)
cv2.imshow('mask and', mask_ANDed)
cv2.imshow('mask or', mask_ORed)
cv2.imshow('mask xor', mask_XORed)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()