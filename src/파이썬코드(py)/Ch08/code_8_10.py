num = 10
divisors = []

for i in range(2, num):
    if num % i == 0:
        divisors.append(i)

print(num,'의 진약수 :', divisors)

############################################

def get_divisors(num):     # num의 약수를 집합형으로 반환함
    divisors = set()
    for i in range(2, num):
        if num % i == 0:
            divisors.add(i)
    return divisors

x = 48
print(x, '의 진약수 :', get_divisors(x))
y = 60
print(y, '의 진약수 :', get_divisors(y))

############################################

A = get_divisors(x)
B = get_divisors(y)

print(A.intersection(B))
print(x, y,'의 최대공약수 :', max(A.intersection(B)))