#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 6.9 함수 안에서 전역변수 사용하기 : global 키워드, 156쪽
#
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

area = 0
r = float(input("원의 반지름: "))
area = calculate_area(r)
print(area)