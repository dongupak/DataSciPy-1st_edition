#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 14-2 데이터 80%로 학습하여 예측한 결과와 실제 데이터 비교, 382쪽
#
import numpy as np 
from sklearn import linear_model  # scikit-learn 모듈을 가져온다
from sklearn import datasets
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()
regr = linear_model.LinearRegression() 
# 학습 데이터와 테스트 데이터를 분리한다. 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(diabetes.data,
                                                    diabetes.target,
                                                    test_size=0.2) 
regr.fit(X_train, y_train)
print(regr.coef_, regr.intercept_)

y_pred = regr.predict(X_test)

plt.scatter(y_pred, y_test)
plt.show()