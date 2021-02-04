#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 6.6 함수에 여러 개의 값을 넘겨주는 고급 기능, 151쪽
#
def get_sum(start, end):  # start, end를 매개변수로하여 인자를 받는다
    s = 0
    for i in range(start, end + 1):  # start부터 end까지 정수의 합을 구함
        s += i
    return s  # start부터 end까지 수의 합을 반환한다

print(get_sum(1, 100))  # 1에서 100까지 정수의 합 55를 출력한다