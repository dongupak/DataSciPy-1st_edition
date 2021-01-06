def print_counter():
    print('counter =', counter)  # 함수 내부의 counter 값


counter = 100
print_counter()
print('counter =', counter)      # 함수 외부의 counter 값

######################################################


def print_counter():
    counter = 200
    print('counter =', counter)  # 함수 내부의 counter 값


counter = 100
print_counter()
print('counter =', counter)      # 함수 외부의 counter 값

