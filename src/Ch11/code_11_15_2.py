#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 11.15 한 화면에 여러 그래프 그리기 : subplots(), 299쪽
#
import matplotlib.pyplot as plt 

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
plt.show()