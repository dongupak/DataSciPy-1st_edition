import numpy as np
import matplotlib.pyplot as plt
data1 = [1, 2, 3, 4, 5]
data2 = [2, 3, 4, 5, 6]
 
plt.boxplot([ data1, data2 ] )
plt.show()

plt.boxplot(np.array([ data1, data2 ]) )
plt.show()
