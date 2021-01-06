def print_counter():
    global counter      # 함수 외부의 전역변수 counter를 사용하겠다는 선언
    counter = 200
    print('counter =', counter)  # 함수 내부의 counter 값

counter = 100
print_counter()
print('counter =', counter)      # 함수 외부의 counter 값

################################################################


def calculate_area(radius):
    global area
    area = 3.14 * radius ** 2
    return


area = 0
r = float(input("원의 반지름: "))
calculate_area(r)
print(area)

