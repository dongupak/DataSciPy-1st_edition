principal = 10000000
years = 5
interest_rate = 0.03
money = principal * (1.0 + interest_rate) ** years

print('원금:  ', principal)
print('이율:  ', interest_rate)
print('기간:  ', years)
print('수령금액: ', money)
