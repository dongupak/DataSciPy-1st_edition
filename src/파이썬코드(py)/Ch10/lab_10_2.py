#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 10-2 여러 사람의 BMI를 빠르고 간편하게 계산하기, 256쪽
#
import numpy as np 
 
heights = [ 1.83, 1.76, 1.69, 1.86, 1.77, 1.73 ] 
weights = [ 86, 74, 59, 95, 80, 68 ] 
 
np_heights = np.array(heights) 
np_weights = np.array(weights) 
 
bmi = np_weights/(np_heights**2) 
print('대상자들의 키:', np_heights)
print('대상자들의 몸무게:', np_weights)
print('대상자들의 BMI')
print(bmi)