#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 6-6 거북이에게 이차함수를 그리게 하자, 162쪽
#
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)  # 터틀 그래픽의 그리기 속도를 가장 빠르게 한다

def f(x):  # 2차 함수를 만든다
    return x ** 2 + 1

t.goto(200, 0)
t.goto(0, 0)
t.goto(0, 200)
t.goto(0, 0)

for x in range(150):
    t.goto(x, int(0.01 * f(x)))
    
turtle.done()