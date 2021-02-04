#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 6-2 n-각형을 그리는 함수 만들어보기, 154쪽
#
import turtle

t = turtle.Turtle()

# n-각형을 그리는 함수를 정의한다.
def n_polygon(n, length):
    for i in range(n):
        t.forward(length)
        t.left(360 // n)  # 정수 나눗셈은 //으로 한다.

for i in range(20):
    t.left(30)
    n_polygon(4, 100)
turtle.done()