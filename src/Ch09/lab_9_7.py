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