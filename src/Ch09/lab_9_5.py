import re 

# 멀티라인 텍스트는 세 개의 따옴표를 사용하여 표현한다
text = '''101 COM PythonProgramming 
102 MAT LinearAlgebra 
103 ENG ComputerEnglish''' 
 
s = re.findall('\d+', text) 
print(s)