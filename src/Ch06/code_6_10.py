def order(num, pickle, onion):
    print('햄버거 {0} 개 - 피클 {1}, 양파 {2}'.format(num, pickle, onion))


order(1, False, True)

######################################################################


def order(num, pickle=True, onion=True):
    print('햄버거 {0} 개 - 피클 {1}, 양파 {2}'.format(num, pickle, onion))


order(1, pickle=False, onion=True)
order(2)  # 햄버거 2개를 주문, 디폴트로 pickle, onion 값은 True임
