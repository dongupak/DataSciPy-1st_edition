import pandas as pd

weather = pd.read_csv('d:/data/weather.csv', index_col = 0, encoding='CP949')
weather.fillna(0, inplace = True)  # 결손값을 0으로 채움, inplace를 True로 설정해 원본 데이터를 수정

print(weather.loc['2012-02-11'])

############################################

weather.fillna( weather['평균풍속'].mean(), inplace = True)
print(weather.loc['2012-02-11'])