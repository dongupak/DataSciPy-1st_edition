#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 3-2 화씨온도를 섭씨온도로 변환하기, 76쪽
#
fahrenheit = float(input("화씨온도: "))
celsius = (fahrenheit - 32.0) * 5.0 / 9.0
print("섭씨온도:", celsius)