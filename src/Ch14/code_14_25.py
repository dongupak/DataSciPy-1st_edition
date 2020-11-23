import pandas as pd 
import seaborn as sns    # 시각화를 위하여 Seaborn 라이브러리를 이용함
import matplotlib.pyplot as plt
import numpy as np

life = pd.read_csv('d:/data/life_expectancy.csv')

life.dropna(inplace = True)

X = life[['Alcohol', 'Percentage expenditure', 'Polio', 
          'BMI', 'GDP', 'Thinness 1-19 years']]
y = life['Life expectancy']

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

from sklearn.linear_model import LinearRegression
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
y_test_predict = lin_model.predict(X_test)

from sklearn.metrics import mean_squared_error
y_test_predict = lin_model.predict(X_test) 
rmse = np.sqrt(mean_squared_error(y_test, y_test_predict))
print('RMSE =', rmse) 

plt.scatter(y_test, y_test_predict)
plt.show()
