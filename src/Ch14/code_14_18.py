#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.18 k-NN 알고리즘을 적용해보자, 388쪽
#
# (80:20)으로 분할한다. 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 

iris = load_iris() 
X_train,X_test,y_train,y_test = train_test_split(iris.data, iris.target,test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier 
from sklearn import metrics 

num_neigh = 1
knn = KNeighborsClassifier(n_neighbors = num_neigh) 
knn.fit(X_train, y_train) 
y_pred = knn.predict(X_test) 
scores = metrics.accuracy_score(y_test, y_pred) 
print('n_neighbors가 {0:d}일때 정확도: {1:.3f}'.format(num_neigh, scores))