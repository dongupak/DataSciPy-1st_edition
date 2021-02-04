#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 9.7 정보를 한눈에 보여주는 워드 클라우드 , 232쪽
#
import wikipedia

# 위키백과 사전의 컨텐츠 제목을 명시해 준다
wiki = wikipedia.page('Artificial intelligence')
# 이 페이지의 텍스트 컨텐츠를 추출하도록 한다
text = wiki.content