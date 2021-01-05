#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.12 당뇨병 예제를 학습 데이터와 테스트 데이터로 구분하자, 381쪽
#
from sklearn import datasets 
from sklearn import linear_model 
import numpy as np 
from sklearn.model_selection import train_test_split
 
# 당뇨병 데이터 세트를 sklearn의 데이터집합으로부터 읽어들인다. 
diabetes = datasets.load_diabetes()
regr = linear_model.LinearRegression() 

X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target,
                                                    test_size = 0.2) 
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)

print(y_pred)
print(y_test)