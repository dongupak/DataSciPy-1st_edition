#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 9-7 패스워드 검사 프로그램을 만들자, 241쪽
#
import re 

while True: 
    password = input("패스워드를 입력하세요 : "); 
    if len(password)<8 or not re.search("[a-z]", password) or \
        not re.search("[A-Z]", password) or \
        not re.search("[0-9]", password) or not re.search("[_@$!]", password): 
        print("유효하지 않은 패스워드!") 
    else: 
        print("유효한 패스워드") 
        break