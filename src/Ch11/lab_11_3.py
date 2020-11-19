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