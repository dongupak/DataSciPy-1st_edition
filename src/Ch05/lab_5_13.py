#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 5-13 창업자를 위한 기능 : 모든 샌드위치 종류 출력하기, 136쪽
#
breads = ["호밀빵", "위트", "화이트"]
meats = ["미트볼", "소시지", "닭가슴살"]
vegis = ["양상추", "토마토", "오이"]
sauces = ["마요네즈", "허니 머스타드", "칠리"]

print('달수네 샌드위치 가게의 가능한 조합')
for b in breads:
    for m in meats:
        for v in vegis:
            for s in sauces:
                print(b + " + " + m + " + " + v + " + " + s)