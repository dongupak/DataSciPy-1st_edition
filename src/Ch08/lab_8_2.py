#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 8-2 영한 사전을 만들어 보자, 205쪽
#
print("사전 프로그램 시작... 종료는 q를 입력")
dictionary = {}

while True:
    st = input('$ ')
    command = st[0]       # 첫 입력 문자를 추출한다
    if command == '<':
        st = st[1:]
        inputStr = st.split(':')
        if len(inputStr) < 2 :
            print('입력 오류가 발생했습니다.')
        else:
            dictionary[inputStr[0].strip()] = inputStr[1].strip()
    elif command == '>':
        st = st[1:]
        inputStr = st.strip()
        if inputStr in dictionary:
            print(dictionary[inputStr])
        else :
            print('{}가 사전에 없습니다.'.format(inputStr))
    elif command == 'q':
       break
    else :
        print('입력 오류가 발생했습니다.')
print("사전 프로그램을 종료합니다.")