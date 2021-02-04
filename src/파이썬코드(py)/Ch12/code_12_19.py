#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.19 데이터 구조를 변경해 보자, 328쪽
#
import pandas as pd 

df_1 = pd.DataFrame({'item' : ['ring0', 'ring0', 'ring1', 'ring1'], 
                     'type' : ['Gold', 'Silver', 'Gold', 'Bronze'], 
                     'price': [20000, 10000, 50000, 30000]})

df_2 = df_1.pivot(index='item', columns='type', values='price') 
print(df_2)