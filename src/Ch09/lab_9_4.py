import random 

n_digits = int(input('몇 자리의 비밀번호를 원하십니까? '))
               
otp = '' 
for i in range(n_digits) : 
      otp += str(random.randrange(0, 10))
      
print(otp)