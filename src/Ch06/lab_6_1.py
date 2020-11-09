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
