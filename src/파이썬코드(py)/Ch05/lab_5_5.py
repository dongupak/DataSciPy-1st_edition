#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 5-5 반복을 이용하여 팩토리얼을 계산하기, 126쪽
#
n = int(input("정수를 입력하시오: ")) 
fact = 1 
for i in range(1, n+1): 
    fact = fact * i 

print(n, "!은", fact, "이다.")