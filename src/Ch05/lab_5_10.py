total = 0 
answer = 'yes' 
while answer == 'yes': 
    number = int(input('숫자를 입력하시오: ')) 
    total = total + number 
    answer = input('계속?(yes/no): ') 

print('합계는 : ', total)
