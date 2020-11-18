import re 
 
txt = 'abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다.'
output = re.findall('\S+@[a-z.]+', txt)
print('추출된 이메일 :', output)