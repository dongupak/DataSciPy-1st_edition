#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 9-6 이메일 주소를 분석해 보자, 240쪽
#
import re 
 
txt = 'abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다.'
output = re.findall('\S+@[a-z.]+', txt)
print('추출된 이메일 :', output)