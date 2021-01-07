#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 7-1 입력을 받아 맛있는 과일의 리스트를 만들어 보자, 175쪽
#
fruits = []
 
name = input('좋아하는 과일의 이름을 입력하시오: ')
fruits.append(name)
name = input('좋아하는 과일의 이름을 입력하시오: ')
fruits.append(name)
name = input('좋아하는 과일의 이름을 입력하시오: ')
fruits.append(name)
 
name = input('과일의 이름을 입력하세요: ')
if name in fruits:
    print('이 과일은 당신이 좋아하는 과일입니다.')
else:
    print('이 과일은 당신이 좋아하는 과일이 아닙니다.')