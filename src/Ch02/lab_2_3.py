#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 2-3 터틀 그래픽으로 피자그리기, 51쪽
#
import turtle

t = turtle.Turtle()
t.shape('turtle')

radius = 100
t.circle(radius)           # 반지름이 100인 원을 그린다.

radius = 200
t.circle(radius)           # 반지름이 200인 원을 그린다.

turtle.done()