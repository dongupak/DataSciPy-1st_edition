#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 6-1 사각형을 그리는 함수 만들어보기, 153쪽
#
import turtle

t = turtle.Turtle()
t.shape("turtle")

def square(length):  # length는 한변의 길이
    for i in range(4):
        t.forward(length)
        t.left(90)


square(100)  # square() 함수를 호출한다.
square(200)  # 호출시 인자값을 100, 200, 300으로 다르게 한다
square(300)
turtle.done()