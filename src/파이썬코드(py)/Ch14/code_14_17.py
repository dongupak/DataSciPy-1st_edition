#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.17 k-NN 알고리즘을 적용할 데이터를 살펴보자, 387쪽
#
from sklearn.datasets import load_iris 
iris = load_iris() 

print(iris.feature_names) # 4개의 특징 이름을 출력한다.

# 정수는 꽃의 종류를 나타낸다.: 0 = setosa, 1=versicolor, 2=virginica 
print(iris.target)