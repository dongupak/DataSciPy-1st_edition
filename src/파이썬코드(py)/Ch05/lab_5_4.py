#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 5-4 술에 취한 거북이를 그리는 랜덤 함수, 125쪽
#
import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for i in range(30):
    length = random.randint(1, 100)
    t.forward(length)
    angle = random.randint(-180, 180)
    t.right(angle)
turtle.done()