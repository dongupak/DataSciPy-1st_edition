#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.16 아름다운 붓꽃의 종류를 분류할 준비를 해보자, 386쪽
#
from sklearn.datasets import load_iris 
iris = load_iris() 
print(iris.data)