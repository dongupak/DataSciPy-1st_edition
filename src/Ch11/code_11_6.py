#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 11.6 하나의 차트에 여러 개의 데이터를 그려보자, 288쪽
#
import matplotlib.pyplot as plt 
 
x = [x for x in range(20)]     # 0에서 20까지의 정수를 생성
y = [x**2 for x in range(20)]  # 0에서 20까지의 정수 x에 대해 x 제곱값을 생성
z = [x**3 for x in range(20)]  # 0에서 20까지의 정수 x에 대해 x 세제곱값을 생성 
 
plt.plot(x, x, label='linear')    # 각 선에 대한 레이블
plt.plot(x, y, label='quadratic') 
plt.plot(x, z, label='qubic') 
 
plt.xlabel('x label')      # x 축의 레이블
plt.ylabel('y label')      # y 축의 레이블
plt.title("My Plot") 
plt.legend()               # 디폴트 위치에 범례를 표시한다
plt.show()