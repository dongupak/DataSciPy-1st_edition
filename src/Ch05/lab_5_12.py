#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 5-12 암산 문제를 만들어보자, 135쪽
#
import random

while True:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    print(x, '+', y, '=', end=' ')
    answer = int(input())
    if answer == x + y:
        print('잘했어요!!')
    else:
        print('정답은', x + y, '입니다. 다음번에는 잘할 수 있죠?')