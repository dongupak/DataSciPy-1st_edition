#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.10 데이터 가시화하기, 317쪽
#
import pandas as pd
import matplotlib.pyplot as plt 

countries_df = pd.read_csv('d:/data/countries.csv', index_col = 0)

# pie 모양 차트를 사용할 때 필요한 코드
#countries_df['population'].plot(kind='pie')
# bar 차트를 사용할 때 필요한 코드
countries_df['population'].plot(kind='bar', color=('b', 'darkorange', 'g', 'r', 'm') )
plt.show()