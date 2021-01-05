#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 11.9 데이터를 점으로 표현하는 산포도 그래프 그리기, 292쪽
#
import matplotlib.pyplot as plt 
import numpy as np 
 
xData = np.arange(20, 50) 
yData = xData + 2*np.random.randn(30)   # xData에 randn() 함수로 잡음을 섞는다.
                                        # 잡음은 정규분포로 만들어 질 것이다.
 
plt.scatter(xData, yData) 
plt.title('Real Age vs Physical Age') 
plt.xlabel('Real Age') 
plt.ylabel('Physical Age') 
 
plt.savefig("age.png", dpi=600)
plt.show()