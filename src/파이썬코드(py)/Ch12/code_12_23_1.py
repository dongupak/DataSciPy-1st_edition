#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.23 데이터를 크기에 따라 나열하자 : 정렬, 334쪽
#
import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv('d:/data/countries.csv', index_col = 0)
sorted = countries_df.sort_values('population')
print(sorted)