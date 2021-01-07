#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 12-1 울릉도는 몇 월에 바람이 가장 강할까?, 311쪽
#
import csv
import matplotlib.pyplot as plt 
 
f = open('d:/data/weather.csv')            # CSV 파일 열어 f에 저장 
data = csv.reader(f)                       # reader() 함수로 읽기
header = next(data)                        # 헤더를 제거

monthly_wind = [ 0 for x in range(12) ]    # 매달 풍속을 담을 리스트
days_counted = [ 0 for x in range(12) ]    # 각 달마다 측정된 일수

for row in data: 
    month = int(row[0][5:7])               # 0번 열에서 달 정보 추출
    if row[3] !=  '' :                     # 풍속 데이터 존재하는지 확인
        wind = float(row[3])               # 풍속을 얻어 온다.
        monthly_wind[month-1] += wind      # 해당 달에 풍속 데이터 추가
        days_counted[month-1] += 1         # 해당 달의 일수를 증가

for i in range(12) :
    monthly_wind[i] /= days_counted[i]   # 일수로 나누어 월평균 구하기
      
plt.plot(monthly_wind, 'blue') 
plt.show()

f.close()                                  # 파일을 닫는다.