# 1
score = int(input("성적을 입력하시오: "))
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")

# 2
num = int(input("양의 정수를 입력하시오: "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# 3
num = int(input("정수를 입력하시오: "))

if num < 0:
    print("음수입니다.")
else:
    print("양수입니다.")
    if num % 2 == 0 :
        print("짝수입니다.")
    else:
        print("홀수입니다.")