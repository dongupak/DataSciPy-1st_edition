import pandas as pd 
import seaborn as sns    # 시각화를 위하여 Seaborn 라이브러리를 이용함
import matplotlib.pyplot as plt
import numpy as np

life = pd.read_csv('./Life_expectancy.csv')
life = life[['Life expectancy', 'Year', 'Alcohol',
           'Percentage expenditure', 'Total expenditure',
           'Hepatitis B', 'Measles', 'Polio', 'BMI', 'GDP',
           'Thinness 1-19 years', 'Thinness 5-9 years']]

life.dropna(inplace = True)

sns.set(rc={'figure.figsize':(12,10)})
correlation_matrix = life.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)

X = life[['Alcohol', 'Percentage expenditure', 'Polio', 
          'BMI', 'GDP', 'Thinness 1-19 years']]
y = life['Life expectancy']

sns.pairplot(life[['Life expectancy', 'Alcohol', 'Percentage expenditure', 'Measles', 'Polio', 'BMI', 'GDP', 'Thinness 1-19 years']])
plt.show()
