#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 10-5 2차원 배열에서 특정 조건을 만족하는 행만 추출하기, 265쪽
#
import numpy as np 

players = [[170, 76.4], 
           [183, 86.2], 
           [181, 78.5], 
           [176, 80.1]] 

np_players = np.array(players) 

print('몸무게가 80 이상인 선수 정보')
print(np_players[ np_players[:, 1] >= 80.0 ])

print('키가 180 이상인 선수 정보')
print(np_players[ np_players[:, 0] >= 180.0 ])