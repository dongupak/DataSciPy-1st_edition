#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.20 분류기의 정확성을 알아보자, 390쪽
#
from sklearn.datasets import load_iris 
from sklearn.metrics import confusion_matrix
 
iris = load_iris()

y_pred_all = knn.predict(iris.data)
conf_mat = confusion_matrix(iris.target, y_pred_all)
print(conf_mat)

plt.matshow(conf_mat)
plt.show()