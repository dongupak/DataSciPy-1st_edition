#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 11.15 한 화면에 여러 그래프 그리기 : subplots(), 299쪽
#
import matplotlib.pyplot as plt 

# 갯수가 2 x 2개, 크기가 (5, 5) 인치 
fig, ax = plt.subplots(2, 2, figsize=(5, 5)) 
 
ax[0, 0].plot(range(10), 'r') # row=0, col=0 
ax[1, 0].plot(range(10), 'b') # row=1, col=0 
ax[0, 1].plot(range(10), 'g') # row=0, col=1 
ax[1, 1].plot(range(10), 'k') # row=1, col=1 
plt.show()

##############################################
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)