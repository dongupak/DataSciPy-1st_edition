#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 14-1 키가 비슷해도 남,녀의 몸무게는 다를 것 : 다차원 선형회귀, 376쪽
#
import numpy as np 
from sklearn import linear_model 
 
regr = linear_model.LinearRegression() 

# 남자는 0, 여자는 1을 넣어 차원을 추가하였음
# 입력데이터를 2차원으로 만들어야 함 
X = [[164, 1],[167, 1],[165, 0],[170, 0],[179, 0],[163, 1],[159, 0],[166, 1]]             
y = [43, 48, 47, 66, 67, 50, 52, 44]     # y 값은 1차원 데이터
regr.fit(X, y)         # 학습 
print('계수 :', regr.coef_ )
print('절편 :', regr.intercept_)
print('점수 :', regr.score(X, y))
print('은지와 동민이의 추정 몸무게 :', regr.predict([[166, 1], [166, 0]]))