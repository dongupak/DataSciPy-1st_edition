st = 'I love Python Programming'  # 출력을 위한 문자열
for ch in st:
    if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        continue                  # 모음일 경우 아래 출력을 건너뛴다
    print(ch, end='')
