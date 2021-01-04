#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 9.11 정규식에서 특정 문자를 대체하는 함수 : sub(), 242쪽
#
import re

s = 'My lucky number 2 7 99'

def hash_by_mult_and_modulo(m):        
    n = int(m.group())                 # 매칭된 문자열을 가져와서 정수로 변환
    return str(n * 23435 % 973)        # 숫자에 해시함수를 적용하고 문자열로 만들어 반환

print(re.sub('[0-9]+', hash_by_mult_and_modulo, s))