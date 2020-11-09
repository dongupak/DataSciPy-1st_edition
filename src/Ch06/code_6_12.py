def factorial(n):  # n!의 재귀적 구현
    if n <= 1:  # 종료 조건이 반드시 필요하다
        return 1
    else:
        return n * factorial(n - 1)  # n * (n-1)! 정의에 따른 구현


print('4! = ', factorial(4))  # 인자로 4를 넣어 호출
