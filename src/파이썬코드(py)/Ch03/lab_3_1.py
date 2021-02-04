#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 3-1 거북이 그래픽으로 숫자를 입력받아 다각형을 그리자, 75쪽
#
import turtle

t = turtle.Turtle()
t.shape("turtle")
n = int(input("몇각형을 그리시겠어요?(3-6): "))

for i in range(n):  # n회만큼 아래의 두 문장을 반복수행한다
    t.forward(100)
    t.left(360 // n)  # 여기서 나눗셈 연산자인 //을 사용한다

turtle.done()