#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.10 데이터 가시화하기, 317쪽
#
import pandas as pd
import matplotlib.pyplot as plt 

weather_df = pd.read_csv('d:/data/weather.csv', index_col = 0, encoding='CP949')
weather_df['평균풍속'].plot(kind='hist', bins=33)
plt.show()