#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 12.4 CSV 데이터의 내용을 읽어 보자, 309쪽
#
import csv     
 
f = open('d:/data/weather.csv')  # CSV 파일을 열어서 f에 저장한다. 
data = csv.reader(f)             # reader() 함수를 이용하여 읽는다. 
for row in data: 
    print(row) 
f.close()