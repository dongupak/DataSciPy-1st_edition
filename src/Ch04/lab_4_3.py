#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 4-3 거북이 제어하기, 101쪽
#
import turtle

t = turtle.Turtle()
# 커서의 모양을 거북이로 한다.
t.shape("turtle")

# 거북이가 그리는 선의 두께를 3으로 한다.
t.width(3)
# 거북이를 3배 확대한다.
t.shapesize(3, 3)

# 무한 루프로 진입한다. 이 루프는 Ctrl+C를 입력받아 종료된다.
while True:
    command = input("명령을 입력하시오: ")
    if command == "l":  # 사용자가 "l"을 입력하였으면
        t.left(90)  # 왼쪽으로 90도 회전
        t.forward(100)
    if command == "r":  # 사용자가 "r"을 입력하였으면
        t.right(90)  # 오른쪽으로 90도 회전
        t.forward(100)