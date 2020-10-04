# 12.4 CSV 데이터의 내용을 읽어 보자
## weather.csv 파일을 통해 날씨 데이터 읽어오기

import csv     
 
f = open('d:/data/weather.csv')  # CSV 파일을 열어서 f에 저장한다. 
data = csv.reader(f)             # reader() 함수를 이용하여 읽는다.
header = next(data)
for row in data: 
    print(row) 
f.close()
