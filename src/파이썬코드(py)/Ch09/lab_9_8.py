#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 9-8 트윗 메시지를 깔끔하게 정제하자, 243쪽
#
import re 
tweet = input('트윗을 입력하시오: ') 
tweet = re.sub('RT', '', tweet)    # RT 문자열을 삭제
tweet = re.sub('#\S+', '', tweet)  # 해시(#)다음에 나타나는 문자열을 삭제
tweet = re.sub('@\S+', '', tweet)  # 앳사인(@)다음에 나타나는 문자열을 삭제
print(tweet)