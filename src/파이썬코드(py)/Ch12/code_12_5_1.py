#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.5 CSV에서 원하는 데이터를 뽑아 보자, 310쪽
#
import csv     
 
f = open('d:/data/weather.csv')  # CSV 파일을 열어서 f에 저장한다. 
data = csv.reader(f)             # reader() 함수를 이용하여 읽는다.
header = next(data)
for row in data: 
    print(row[3], end=',') 
f.close()