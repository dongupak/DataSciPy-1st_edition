import re 
tweet = input('트윗을 입력하시오: ') 
tweet = re.sub('RT', '', tweet)    # RT 문자열을 삭제
tweet = re.sub('#\S+', '', tweet)  # 해시(#)다음에 나타나는 문자열을 삭제
tweet = re.sub('@\S+', '', tweet)  # 앳사인(@)다음에 나타나는 문자열을 삭제
print(tweet)