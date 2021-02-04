#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 6.5 함수에 일을 시키고 그 값을 받아오도록 하자, 150쪽
#
def calculate_area(radius):
    area = 3.14 * radius**2
    return area               # 이전 줄에서 구한 area 값을 호출문에 돌려준다

c_area = calculate_area(5.0)  # calculate_are() 함수가 계산한 값을 c_area에 저장
print(c_area)
c_area = calculate_area(10.0)  # calculate_are() 함수가 계산한 값을 c_area에 저장
print(c_area)
area_sum = calculate_area(5.0) + calculate_area(10.0)
print(area_sum)