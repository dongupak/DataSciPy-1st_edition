import matplotlib.pyplot as plt 
 
books = [ 1, 6, 2, 3, 1, 2, 0, 2 ] 

# 6개의 빈을 이용하여 books 안에 저장된 자료의 히스토그램 그리기
plt.hist(books, bins = 6)  

plt.xlabel("books") 
plt.ylabel("frequency") 
plt.show()