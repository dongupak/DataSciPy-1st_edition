from sklearn.datasets import load_iris 
iris = load_iris() 

print(iris.feature_names) # 4개의 특징 이름을 출력한다.

# 정수는 꽃의 종류를 나타낸다.: 0 = setosa, 1=versicolor, 2=virginica 
print(iris.target)