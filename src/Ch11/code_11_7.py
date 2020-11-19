from matplotlib import pyplot as plt 
 
# 1인당 국민소득 
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010] 
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3] 
 
plt.bar(range(len(years)), gdp) 
 
plt.title("GDP per capita")   # 제목을 설정한다. 
plt.ylabel("dollars")         # y축에 레이블를 붙인다. 
 
# y축에 틱을 붙인다. 
plt.xticks(range(len(years)), years) 
plt.show()