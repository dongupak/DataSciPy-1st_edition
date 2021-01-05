#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.12 새로운 열을 쉽게 생성해 보자, 319쪽
#
import pandas as pd
import matplotlib.pyplot as plt 

countries_df = pd.read_csv('d:/data/countries.csv', index_col = 0)
countries_df['density'] = countries_df['population'] / countries_df['area']
print(countries_df)