#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 5-10 간단한 코드로 멋진 나선형 도형 그려보기, 133쪽
#
total = 0 
answer = 'yes' 
while answer == 'yes': 
    number = int(input('숫자를 입력하시오: ')) 
    total = total + number 
    answer = input('계속?(yes/no): ') 

print('합계는 : ', total)