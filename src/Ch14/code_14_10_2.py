from sklearn import datasets 
from sklearn import linear_model 
import numpy as np 
from sklearn.model_selection import train_test_split
 
# 당뇨병 데이터 세트를 sklearn의 데이터집합으로부터 읽어들인다. 
diabetes = datasets.load_diabetes()

X_train, X_test, y_train, y_test = train_test_split(diabetes.data[:, np.newaxis, 2],
                                                    diabetes.target,
                                                    test_size = 0.2) 
regr = linear_model.LinearRegression() 
regr.fit(X_train, y_train)

score = regr.score(X_train, y_train)
print(score)
score = regr.score(X_test, y_test)
print(score)