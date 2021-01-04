#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 6.9 함수 안에서 전역변수 사용하기 : global 키워드, 156쪽
#
def print_counter():
    global counter      # 함수 외부의 전역변수 counter를 사용하겠다는 선언
    counter = 200
    print('counter =', counter)  # 함수 내부의 counter 값

counter = 100
print_counter()
print('counter =', counter)      # 함수 외부의 counter 값