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

import matplotlib.pyplot as plt
plt.hist2d(iris.target, y_pred_all, bins=(3,3), cmap=plt.cm.jet)
plt.show()

from sklearn.metrics import confusion_matrix
conf_mat = confusion_matrix(iris.target, y_pred_all)
print(conf_mat)

plt.matshow(conf_mat)
plt.show()
