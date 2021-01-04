#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 9.7 정보를 한눈에 보여주는 워드 클라우드 , 232쪽
#
from wordcloud import WordCloud

# 워드 클라우드를 생성하기 위해 위의 코드를 삽입할 것
wordcloud = WordCloud(width = 2000, height = 1500).generate(text)