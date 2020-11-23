import pandas as pd 
import seaborn as sns    # 시각화를 위하여 Seaborn 라이브러리를 이용함

life = pd.read_csv('d:/data/life_expectancy.csv')
#print(life.head())

life = life[['Life expectancy', 'Year', 'Alcohol',
           'Percentage expenditure', 'Total expenditure',
           'Hepatitis B', 'Measles', 'Polio', 'BMI', 'GDP',
           'Thinness 1-19 years', 'Thinness 5-9 years']]
#print(life)

#print( life.shape )
#print( life.isnull().sum() )

life.dropna(inplace = True)
print(life.shape)
