num = int(input("정수를 입력하시오: "))
if num >= 0:         # 반드시 들여쓰기를 하여 블럭을 생성
    if num == 0:     # 블럭 내에서 세부적인 조건을 한 번 더 검사
        print("0입니다.")
    else:
        print("양수입니다.")
else:
    print("음수입니다.")
