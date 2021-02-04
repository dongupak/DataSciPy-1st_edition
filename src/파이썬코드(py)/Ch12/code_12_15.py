#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.15 데이터를 특정한 값에 기반하여 묶는 기능 : 그룹핑 , 323쪽
#
import pandas as pd
weather = pd.read_csv('d:/data/weather.csv', encoding='CP949')
weather['month'] = pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean()

print(means)

##############################

sum_data = weather.groupby('month').sum()
print(sum_data)