#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 11.4 맷플롯립 코드 살펴 보기, 285쪽
#
import matplotlib.pyplot as plt 
 
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010] 
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 22105.3]

# 상단의 코드: x축: 연도, y축: GDP
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# 하단의 코드: x축: GDP, y축: 연도
# plt.plot(gdp, years, color='red', marker='o', linestyle='solid')

plt.title("GDP per capita")

plt.ylabel("dollars")
plt.savefig("gdp_per_capita.png", dpi=600)
plt.show()