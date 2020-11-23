from sklearn import datasets 
from sklearn import linear_model 
import numpy as np 

regr = linear_model.LinearRegression()
 
# 당뇨병 데이터 세트를 sklearn의 데이터집합으로부터 읽어들인다. 
diabetes = datasets.load_diabetes()

X = diabetes.data[:, np.newaxis, 2]

regr.fit(X, diabetes.target)         # 학습을 통한 선형회귀 모델을 생성 
print(regr.coef_, regr.intercept_)