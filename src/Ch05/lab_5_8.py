#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 5-8 while 문으로 별 그리기를 해보자, 131쪽
#
import turtle

t = turtle.Turtle()
t.shape("turtle")
i = 0
while i < 5:        # 5개의 선분을 그리기 위하여 5회 반복
    t.forward(50)   # 50 픽셀 길이의 선분을 그린다
    t.right(144)    # 144도 거북을 회전시킨다
    i = i + 1       # 변수 i를 1만큼 증가시킨다
turtle.done()