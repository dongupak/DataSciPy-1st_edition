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