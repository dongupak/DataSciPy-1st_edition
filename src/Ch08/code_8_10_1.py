#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 8.10 두 수의 약수와 최대공약수 그리고 프로그래밍적인 사고, 213쪽
#
num = 10
divisors = []

for i in range(2, num):
    if num % i == 0:
        divisors.append(i)

print(num,'의 진약수 :', divisors)