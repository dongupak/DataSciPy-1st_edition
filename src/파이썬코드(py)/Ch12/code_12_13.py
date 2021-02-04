#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.13 데이터를 간편하게 분석할 수 있는 기능이 있다, 320쪽
#
import pandas as pd
weather = pd.read_csv('d:/data/weather.csv', index_col = 0, encoding='CP949')

print(weather.describe())

print('평균 분석 -----------------------------')
print(weather.mean())
print('표준편차  분석 -----------------------------')
print(weather.std())