import matplotlib.pyplot as plt 
times = [8, 14, 2]

timelabels = ["Sleep", "Study", "Play"]

# autopct로 백분율을 표시할 때 소수점 2번째 자리까지 표시하게 한다.
# labels 매개 변수에 timelabels 리스트를 전달한다.
plt.pie(times, labels = timelabels, autopct = "%.2f") 
plt.show()