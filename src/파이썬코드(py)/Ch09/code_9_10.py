#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 9.10 정규식을 활용해서 멋지게 검색을 하자, 238쪽
#
import re 

f = open('d:/data/UNDHR.txt')     # 현재 폴더에 있는 파일을 읽어온다.

for line in f: 
    line = line.rstrip()
    if re.search('^\([0-9]+\)', line) : 
        print(line)