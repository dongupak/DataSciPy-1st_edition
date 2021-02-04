#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.17 빠진 값을 찾고 삭제하기, 326쪽
#
import pandas as pd

weather = pd.read_csv('d:/data/weather.csv', index_col = 0, encoding='CP949')
missing_data = weather [ weather['평균풍속'].isna() ] 
print(missing_data)