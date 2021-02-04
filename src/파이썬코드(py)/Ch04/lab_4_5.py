#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 4-5 랜덤 함수로 동전 던지기 게임을 만들자, 105쪽
#
import random

print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)  # randrange(2)는 0 또는 1을 반환함
if coin == 0:
    print("앞면입니다.")
else:
    print("뒷면입니다.")
print("게임이 종료되었습니다.")