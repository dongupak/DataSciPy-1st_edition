#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.5 CSV에서 원하는 데이터를 뽑아 보자, 310쪽
#
import csv     
 
f = open('d:/data/weather.csv')  # CSV 파일을 열어서 f에 저장한다. 
data = csv.reader(f)             # reader() 함수를 이용하여 읽는다.
header = next(data)

max_wind = 0.0
for row in data:                  # 반복 루프를 사용하여 데이터를 읽는다.
    if row[3] == '' :             # 평균 풍속 데이터가 없는 경우 0을 처리
        wind = 0
    else :
        wind = float(row[3])    # 평균 풍속 데이터를 실수로 변환해 저장
    if max_wind < wind :        # 최대 풍속을 갱신하는지 검사
        max_wind = wind         # 현재까지의 최대 풍속보다 크면 새로 기록

print('지난 10년간 울릉도의 최대 풍속은 ', max_wind, 'm/s')