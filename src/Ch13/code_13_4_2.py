#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 13.4 OpenCV로 이미지 다루어 보자, 344쪽
#
import cv2

img = cv2.imread('d:/data/mandrill.png', 1)
cv2.line(img, (0,0), (200,200), (0,0,255), 5)      # 직선의 시작점과 끝점, 색상, 두께를 지정함
cv2.rectangle(img, (0,200), (200,20), (0,0,0), 5)  # 사각형의 좌표, 색상을 지정
cv2.putText(img, "hello", (70,70), fontFace = 2, fontScale = 1, color = (0,0,0))
cv2.imshow('lined', img)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()