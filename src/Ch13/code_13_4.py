#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 13.4 OpenCV로 이미지 다루어 보자, 344쪽
#
import cv2

img = cv2.imread('d:/data/mandrill.png', 1)
cv2.line(img, (0,0), (200,200), (0,0,255), 5)    # 직선의 시작점과 끝점, 색상, 두께를 지정함
cv2.arrowedLine(img, (0,200), (200,20), (0,0,255), 5)#화살표의 시작점, 끝점, 색상, 두께지정
cv2.imshow('lined', img)

cv2.waitKey(0)
