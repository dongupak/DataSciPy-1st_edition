import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.linear_model import LinearRegression 
from sklearn import datasets 
 
# 당뇨병 데이터 세트를 sklearn의 데이터집합으로부터 읽어들인다. 
diabetes = datasets.load_diabetes()

print('shape of diabetes.data: ', diabetes.data.shape)
print(diabetes.data)

print('입력데이터의 특성들')
print(diabetes.feature_names)

print('target data y:', diabetes.target.shape)
print(diabetes.target)

X = diabetes.data[:, np.newaxis, 2]  # 배열의 차원을 증가시킴
print(X)    # (442, 1) 형태의 행렬이 되었는가 확인