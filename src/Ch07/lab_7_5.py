#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 7-5 함수는 튜플을 돌려줄 수 있다, 191쪽
#
import math 
 
def calCircle(r): 
    # 반지름이 r인 원의 넓이와 둘레를 동시에 반환하는 함수 (area, circum) 
    area = math.pi * r * r 
    circum = 2 * math.pi * r 
    return area, circum    # 튜플을 반환함
 
radius = float(input("원의 반지름을 입력하시오: ")) 
(a, c) = calCircle(radius) 
print("원의 넓이는 "+str(a)+"이고 원의 둘레는"+str(c)+"이다.")