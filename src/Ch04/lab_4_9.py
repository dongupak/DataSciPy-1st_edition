import turtle
t = turtle.Turtle() 
t.shape("turtle") 
 
s = turtle.textinput("", "도형을 입력하시오: ") 
if s == "사각형":
    s = turtle.textinput("", "가로: ")
    w = int(s) 
    s = turtle.textinput("", "세로: ")
    h = int(s) 
    t.forward(w) 
    t.left(90) 
    t.forward(h) 
    t.left(90) 
    t.forward(w) 
    t.left(90) 
    t.forward(h)

# 나머지 부분은 여러분이 완성해 보세요.

turtle.done()
