import re

s = 'My lucky number 2 7 99'

def hash_by_mult_and_modulo(m):        
    n = int(m.group())                 # 매칭된 문자열을 가져와서 정수로 변환
    return str(n * 23435 % 973)        # 숫자에 해시함수를 적용하고 문자열로 만들어 반환

print(re.sub('[0-9]+', hash_by_mult_and_modulo, s))