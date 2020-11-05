import turtle

t = turtle.Turtle()
t.shape("turtle")

# 정삼각형 그리기
for i in range(3):
    t.forward(100)
    t.left(360 / 3)  # 360/3을 통해 120도 왼쪽으로 틀기

# 정사각형을 그리기 위하여 터틀을 이동하기
t.penup()            # 펜 자국이 남지 않도록 펜을 들어서 이동한다
t.goto(200, 0)
t.pendown()          # 이동을 마치면 펜은 내리도록 한다

# 정사각형 그리기
for i in range(4):
    t.forward(100)
    t.left(360 / 4)   # 360/4를 통해 90도 왼쪽으로 틀기
