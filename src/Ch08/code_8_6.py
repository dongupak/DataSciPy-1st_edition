numbers = {2, 1, 3} 
if 1 in numbers:     # 1이라는 항목이 numbers 집합에 있는가 검사
    print("집합 안에 1이 있습니다.")

numbers = {2, 1, 3} 
for x in numbers: 
    print(x, end=" ")

for x in sorted(numbers): 
    print(x, end=" ")