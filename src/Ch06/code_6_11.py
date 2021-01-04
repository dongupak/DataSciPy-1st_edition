#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 6.11 키워드 인자로 더욱더 고급지게 함수 활용하기, 158쪽
#
def power(base, exponent):
    return base**exponent   # base가 밑이고, exponent가 지수값이다

power(2, 10)
power(10, 2)
power(base=2, exponent=10)
power(exponent=10, base=2)