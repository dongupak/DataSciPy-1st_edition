#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.9 사이킷런의 당뇨병 예제와 학습 데이터 생성, 377쪽
#
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