import turtle 
t = turtle.Turtle() 
t.shape("turtle") 
i = 0 
while i < 18:        # 5개의 선분을 그리기 위하여 5회 반복
    t.forward(150)   # 50 픽셀 길이의 선분을 그린다
    t.right(140)    # 144도 거북을 회전시킨다
    i = i + 1       # 변수 i를 1만큼 증가시킨다
