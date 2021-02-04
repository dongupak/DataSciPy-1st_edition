def get_sum(start, end):  # start, end를 매개변수로하여 인자를 받는다
    s = 0
    for i in range(start, end + 1):  # start부터 end까지 정수의 합을 구함
        s += i
    return s  # start부터 end까지 수의 합을 반환한다


print(get_sum(1, 10))  # 1에서 10까지 정수의 합 55를 출력한다

x = get_sum(1, 10)  # 1과 10이 인자가 된다.
print('x =', x)

y = get_sum(1, 20)  # 1과 20이 인자가 된다.
print('y =', y)

