#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.9 열을 기준으로 데이터 선택하기, 316쪽
#
import pandas as pd 

df_my_index = pd.read_csv('d:/data/countries.csv', index_col = 0)
df_no_index = pd.read_csv('d:/data/countries.csv')
print(df_my_index['population'])
print(df_no_index['population'])