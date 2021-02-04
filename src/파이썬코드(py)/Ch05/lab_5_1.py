#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 5-1 터틀 그래픽으로 여러 개의 원을 그려보자, 122쪽
#
import turtle

t = turtle.Turtle()

for count in range(6):
    t.circle(100)
    t.left(360 / 6)
turtle.done()