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
