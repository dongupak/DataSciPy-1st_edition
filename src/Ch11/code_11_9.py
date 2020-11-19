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