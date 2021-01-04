#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 1.5 프로그래밍을 꼭 알아야 하나, 24쪽
#
from collections import Counter

f = open("d:/mobydick.txt", encoding="utf-8")
count = Counter(f.read().split())
print("단어 출현 횟수 :", count)