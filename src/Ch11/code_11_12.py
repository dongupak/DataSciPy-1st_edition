import numpy as np 
import matplotlib.pyplot as plt 
 
n_bins = 10 
x = np.random.randn(1000) 
y = np.random.randn(1000) 
 
plt.hist(x, n_bins, histtype='bar', color='red')
plt.hist(y, n_bins, histtype='bar', color='blue', alpha=0.3)
plt.show()