import numpy as np 

x = [ i for i in range(100) ]       # 0에서 99까지의 값을 요소로 하는 리스트
y = [ i ** 2 for i in range(100) ]  # 0에서 99까지의 값의 제곱을 요소로 하는 리스트

result = np.corrcoef(x, y)
print(result)