# 12.10 데이터 가시화 하기 
## weather.csv 파일을 읽기

import pandas as pd
import matplotlib.pyplot as plt 

weather_df = pd.read_csv('d:/data/weather.csv', index_col = 0, encoding='CP949')
weather_df['평균풍속'].plot(kind='hist', bins=33)
plt.show()
