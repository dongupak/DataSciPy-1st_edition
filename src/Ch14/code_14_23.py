#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.23 각 특징들 사이의 상관관계를 살펴보자, 393쪽
#
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

life = pd.read_csv('d:/data/life_expectancy.csv')

sns.set(rc={'figure.figsize':(12,10)})
correlation_matrix = life.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)
plt.show()