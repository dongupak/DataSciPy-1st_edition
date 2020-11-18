import numpy as np 

x = [ i for i in range(100) ]
y = [ i ** 2 for i in range(100) ]
z = [ 100 * np.sin(3.14*i/100) for i in range(100) ]

result = np.corrcoef( [x, y, z] )
print(result)