import matplotlib.pyplot as plt

x = [x for x in range(-10, 10)] 
y = [2*t for t in x]            # 2*x를 원소로 가지는 y 함수
plt.plot(x, y, marker='o')      # 선 그래프에 동그라미 표식을 출력

plt.axis([-20, 20, -20, 20])    # 그림을 그릴 영역을 지정함
plt.show()