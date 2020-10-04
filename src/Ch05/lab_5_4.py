import turtle 
t = turtle.Turtle() 
t.shape("turtle") 
 
s = turtle.textinput("도형그리기", "몇각형을 원하시나요:") 
n = int(s) 

s = turtle.textinput("도형그리기", "변의 길이를 입력하세요:") 
l = int(s) 
 
for i in range(n): 
    t.forward(l) 
    t.left(360/n) 
