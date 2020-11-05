under_construction = True
while under_construction:
    response = input("공사가 완료 되었습니까?")
    if response == "예":
        under_construction = False

print("루프를 탈출했습니다.")
