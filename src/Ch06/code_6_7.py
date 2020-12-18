def sort_num(n1, n2):  # 2개의 값을 받아오는 함수
    if n1 < n2:
        return n1, n2  # n1이 더 작으면 n1, n2 순서로 반환
    else:
        return n2, n1  # n2가 더 작으면 n2, n1 순서로 반환


print(sort_num(110, 210))  # 110과 210을 함수의 인자로 전달하고 반환되는 값을 출력
print(sort_num(2100, 80))


def calc(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2  # 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 반환


n1, n2 = 200, 100
t1, t2, t3, t4 = calc(n1, n2)  # 네 개의 값을 반환받기 위해 4개의 변수를 사용함
print(n1, '+', n2, '=', t1)
print(n1, '-', n2, '=', t2)
print(n1, '*', n2, '=', t3)
print(n1, '/', n2, '=', t4)
