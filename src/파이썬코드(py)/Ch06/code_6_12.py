#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 6.12 자신을 호출하는 재귀 함수, 163쪽
#
def factorial(n):  # n!의 재귀적 구현
    if n <= 1:  # 종료 조건이 반드시 필요하다
        return 1
    else:
        return n * factorial(n - 1)  # n * (n-1)! 정의에 따른 구현

print('4! = ', factorial(4))  # 인자로 4를 넣어 호출