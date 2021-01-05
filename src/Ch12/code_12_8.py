#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.8 데이터를 설명하는 인덱스와 컬럼스 객체, 315쪽
#
import pandas as pd 

df = pd.read_csv('d:/data/countries.csv', index_col = 0)
print(df)