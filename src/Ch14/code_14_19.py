#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.19 새로운 꽃에 대해서 모델을 적용하고 분류해 보자, 389쪽
#
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 
 
iris = load_iris() 
knn = KNeighborsClassifier(n_neighbors=6) 
knn.fit(iris.data, iris.target)

classes = {0:'setosa', 1:'versicolor', 2:'virginica'} 
 
# 아직 보지 못한 새로운 데이터를 제시해 보자. 
X = [[3,4,5,2], 
[5,4,2,2]] 
y = knn.predict(X) 
 
print(classes[y[0]]) 
print(classes[y[1]]) 