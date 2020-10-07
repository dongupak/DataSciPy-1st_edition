import turtle

t = turtle.Turtle()
t.shape("turtle")

t.penup()  # 펜을 올려서 그림이 그려지지 않게 한다.
t.goto(100, 100)  # 거북이를 (100, 100)으로 이동시킨다.
t.write("거북이가 여기로 오면 양수입니다.")
t.goto(100, 0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100, -100)
t.write("거북이가 여기로 오면 음수입니다.")

t.goto(0, 0)  # (0, 0) 위치로 거북이를 이동시킨다.
t.pendown()  # 펜을 내려서 그림이 그려지게 한다.

s = turtle.textinput("", "숫자를 입력하시오: ")
n = int(s)

if n > 0:
    t.goto(100, 100)
if n == 0:
    t.goto(100, 0)
if n < 0:
    t.goto(100, -100)

turtle.done()
