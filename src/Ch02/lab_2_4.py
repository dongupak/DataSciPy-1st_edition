#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 2-4 복리 이자 계산하기, 52쪽
#
principal = 10000000
years = 5
interest_rate = 0.03
money = principal * (1.0 + interest_rate) ** years

print('원금:  ', principal)
print('이율:  ', interest_rate)
print('기간:  ', years)
print('수령금액: ', money)