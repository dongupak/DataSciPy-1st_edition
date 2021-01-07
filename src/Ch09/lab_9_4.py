#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 9-4 1회용 패스워드를 만들어 보자, 231쪽
#
import random 

n_digits = int(input('몇 자리의 비밀번호를 원하십니까? '))
               
otp = '' 
for i in range(n_digits) : 
      otp += str(random.randrange(0, 10))
      
print(otp)