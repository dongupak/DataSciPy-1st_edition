#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 5-3 N-각형 그리기, 124쪽
#
import turtle

t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("도형그리기", "몇각형을 원하시나요?:")
n = int(s)

for i in range(n):
    t.forward(100)
    t.left(360 / n)
turtle.done()