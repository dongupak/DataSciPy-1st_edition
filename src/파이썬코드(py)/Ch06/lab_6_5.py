#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 6-5 거북이에게 막대 그래프를 그리게 하자, 161쪽
#
import turtle

def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font = ('Times New Roman', 16, 'bold'))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

data = [120, 56, 309, 220, 156, 23, 98]

t = turtle.Turtle()
t.color("blue")
t.fillcolor("red")
t.pensize(3)

for d in data:
    drawBar(d)

turtle.done()