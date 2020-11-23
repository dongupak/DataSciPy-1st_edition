import pandas as pd
weather = pd.read_csv('d:/data/weather.csv', encoding='CP949')
weather['month'] = pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean()

print(means)

##############################

sum_data = weather.groupby('month').sum()
print(sum_data)