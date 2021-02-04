#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 11-4 서브플롯 이용해 보기, 300쪽
#
import matplotlib.pyplot as plt 
import numpy as np 
 
np.random.seed(19680801) 
data = np.random.randn(2, 100) 
 
fig, axs = plt.subplots(2, 2, figsize=(5, 5)) 

axs[0, 0].hist(data[0]) 
axs[1, 0].scatter(data[0], data[1]) 
axs[0, 1].plot(data[0], data[1]) 
axs[1, 1].hist2d(data[0], data[1]) 
 
plt.show()