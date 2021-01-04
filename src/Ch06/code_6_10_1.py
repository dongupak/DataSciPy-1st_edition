#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 6.10 함수에 쉽게 일을 시키는 디폴트 인자, 157쪽
#
def order(num, pickle, onion):
    print('햄버거 {0} 개 - 피클 {1}, 양파 {2}'.format(num, pickle, onion))


order(1, False, True)