def calculate_area(radius):
    area = 3.14 * radius**2
    return area               # 이전 줄에서 구한 area 값을 호출문에 돌려준다


c_area = calculate_area(5.0)  # calculate_are() 함수가 계산한 값을 c_area에 저장
print(c_area)

