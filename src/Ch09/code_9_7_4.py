#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 9.7 정보를 한눈에 보여주는 워드 클라우드 , 232쪽
#
from wordcloud import WordCloud, STOPWORDS
# 중지어가 제외된 워드 클라우드를 만들자
s_words = STOPWORDS.union( {'one', 'using', 'first', 'two', 'make', 'use'} )
wordcloud = WordCloud(width = 2000, height = 1500, 
                      stopwords = s_words).generate(text)