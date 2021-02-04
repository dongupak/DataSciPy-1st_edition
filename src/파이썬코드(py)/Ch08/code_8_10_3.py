#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 8.10 두 수의 약수와 최대공약수 그리고 프로그래밍적인 사고, 213쪽
#
def get_divisors(num):     # num의 약수를 집합형으로 반환함
    divisors = set()
    for i in range(2, num):
        if num % i == 0:
            divisors.add(i)
    return divisors

x = 48
y = 60

A = get_divisors(x)
B = get_divisors(y)

print(A.intersection(B))
print(x, y,'의 최대공약수 :', max(A.intersection(B)))