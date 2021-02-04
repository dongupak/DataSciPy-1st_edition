#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.24 어떤 특징들이 서로 상관관계가 있을까, 394쪽
#
import pandas as pd 
import seaborn as sns    # 시각화를 위하여 Seaborn 라이브러리를 이용함
import matplotlib.pyplot as plt

life = pd.read_csv('d:/data/life_expectancy.csv')

sns.pairplot(life[['Life expectancy', 'Alcohol', 'Percentage expenditure', 'Measles', 'Polio', 'BMI', 'GDP', 'Thinness 1-19 years']])
plt.show()