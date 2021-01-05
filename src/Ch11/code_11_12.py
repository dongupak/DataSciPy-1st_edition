#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 11.12 겹쳐진 히스토그램도 그리자 : 다중 히스토그램, 295쪽
#
import numpy as np 
import matplotlib.pyplot as plt 
 
n_bins = 10 
x = np.random.randn(1000) 
y = np.random.randn(1000) 
 
plt.hist(x, n_bins, histtype='bar', color='red')
plt.hist(y, n_bins, histtype='bar', color='blue', alpha=0.3)
plt.show()