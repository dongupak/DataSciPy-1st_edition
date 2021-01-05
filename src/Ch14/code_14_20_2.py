#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 14.20 분류기의 정확성을 알아보자, 390쪽
#
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
 
iris = load_iris()

plt.hist2d(iris.target, y_pred_all, bins=(3,3), cmap=plt.cm.jet)
plt.show()