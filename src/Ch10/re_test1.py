import re

txt1 = "Life is too short, you need python."
txt2 = "The best moments of my life."
txt3 = "Life is like a box of chocolates."
txt4 = "My Life My Choice."

print(re.search('Life', txt1))    # 문장내에 Life가 있는가 검사함
