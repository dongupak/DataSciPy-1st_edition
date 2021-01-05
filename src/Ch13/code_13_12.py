#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 13.12 윤곽선을 더 잘 뽑아 낼 수 있을까, 358쪽
#
import cv2

# image를 회색조로 읽어들인다.
img_gray = cv2.imread('d:/data/green_back.png', cv2.IMREAD_GRAYSCALE)

# adaptiveThreshold를 적용한다
# 주변 9x9 픽셀 공간의 평균값 - 5가 임계치가 되고, 이보다 크면 255, 그렇지 않으면 0
img_edge = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY,   blockSize=9, C=0)

# 결과는 윤곽선 픽셀이 드러난다
cv2.imshow('edge', img_edge)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()