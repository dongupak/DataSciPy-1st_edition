#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 7.14 조건이 붙는 리스트 함축 표현도 가능하다, 189쪽
#
s = ["Hello", "12345", "World", "67890"] 
numbers = [x for x in s if x.isdigit()] 
print(numbers)