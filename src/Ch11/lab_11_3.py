#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 11-3 정규분포로 생성된 난수를 눈으로 확인하기, 296쪽
#
import numpy as np 
import matplotlib.pyplot as plt 
 
mu1, sigma1 = 10, 2
mu2, sigma2 = -6, 3

standard_Gauss = np.random.randn(10000)
Gauss1 = mu1 + sigma1 * np.random.randn(10000)
Gauss2 = mu2 + sigma2 * np.random.randn(10000) 

plt.figure(figsize=(10,6)) 
plt.hist(standard_Gauss, bins=50, alpha=0.4) 
plt.hist(Gauss1, bins=50, alpha=0.4)
plt.hist(Gauss2, bins=50, alpha=0.4)

plt.show()