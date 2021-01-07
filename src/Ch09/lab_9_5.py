#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 9-5 학사 코드 추출하기에 도전하자, 239쪽
#
import re 

# 멀티라인 텍스트는 세 개의 따옴표를 사용하여 표현한다
text = '''101 COM PythonProgramming 
102 MAT LinearAlgebra 
103 ENG ComputerEnglish''' 
 
s = re.findall('\d+', text) 
print(s)