import re 

f = open('d:/data/UNDHR.txt')     # 현재 폴더에 있는 파일을 읽어온다.

for line in f: 
    line = line.rstrip()
    if re.search('^\([0-9]+\)', line) : 
        print(line)