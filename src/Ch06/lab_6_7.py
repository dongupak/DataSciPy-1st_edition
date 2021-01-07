#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 6-7 피보나치 함수 계산하기, 164쪽
#
def fibonacci(n):
    if n < 0:  # 입력 오류 검사
        print("잘못된 입력입니다.")
    elif n == 1:  # 재귀호출 중단 조건
        return 0
    elif n == 2:  # 재귀호출 중단 조건
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # 재귀호출

i = int(input("몇 번째 항: "))
print(fibonacci(i))