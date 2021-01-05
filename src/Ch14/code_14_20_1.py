#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.20 분류기의 정확성을 알아보자, 390쪽
#
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn import metrics 
 
iris = load_iris()
num_neigh = 5
knn = KNeighborsClassifier(n_neighbors=num_neigh) 
knn.fit(iris.data, iris.target)

y_pred_all = knn.predict(iris.data)
scores = metrics.accuracy_score(iris.target, y_pred_all)
print('n_neighbors가 {0:d}일때 정확도: {1:.3f}'.format(num_neigh, scores))