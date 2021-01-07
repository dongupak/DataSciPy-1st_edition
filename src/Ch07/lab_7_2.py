#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 7-2 리스트에 도시의 인구를 저장해보자, 177쪽
#
# 인구 통계(단위: 천명) 
Seoul = 9765 
Busan = 3441 
Incheon = 2954 
city_pop = [ Seoul, Busan, Incheon ]    # 변수들로 리스트 생성
print(city_pop)                         # 리스트 데이터를 출력

Daejeon = 1531
city_pop.append(Daejeon)

max_pop = 0
min_pop = 1000000
pop_sum = 0
n = 0

for pop in city_pop:    # 순환문을 돌면서 최댓값, 최솟값을 구한다
    if pop > max_pop :
        max_pop = pop
    if pop < min_pop :
        min_pop = pop
    pop_sum += pop
    n += 1

print('최대 인구:', max_pop)
print('최소 인구:', min_pop)
print('평균 인구:', pop_sum / n)