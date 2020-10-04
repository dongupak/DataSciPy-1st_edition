# 12.10 데이터 가시화 하기 
## countries.csv 파일을 읽기

import pandas as pd
import matplotlib.pyplot as plt 

countries_df = pd.read_csv('d:/data/countries.csv', index_col = 0)

# pie 모양으로 만들때 uncomment 하세요.
#countries_df['population'].plot(kind='pie')
countries_df['population'].plot(kind='bar')
plt.show()
