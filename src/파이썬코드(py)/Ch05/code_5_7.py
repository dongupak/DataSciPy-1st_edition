#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 5.7 조건에 따라 반복해서 실행하는 while 문, 127쪽
#
under_construction = True
while under_construction:
    response = input("공사가 완료 되었습니까?")
    if response == "예":
        under_construction = False

print("루프를 탈출했습니다.")