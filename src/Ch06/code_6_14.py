#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 6.14 나만의 모듈을 만들고 불러서 사용해 보자, 166쪽
#
import my_func

my_func.mf_print("my_func was imported ", 3)  # my_func 모듈의 mf_print() 함수 호출


###############################################################################


import my_func as mf

mf.mf_print('[alias]', 5)  # mf라는 별명을 사용해서 메시지를 5회 반복출력


###############################################################################


from my_func import mf_print

mf_print('-no module name-', 2)  # mf_print()를 호출할 때 my_func.을 사용안해도 됨


###############################################################################


from my_func import *

mf_print('-no module name-', 2)
