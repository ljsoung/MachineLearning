import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# pad 매개변수에 100을 입력하여 제목과 그래프의 간격을 100 픽셀로 설정
# plt.title("Graph Title", fontsize = 16, color = 'blue', fontweight = 'bold', loc = 'left', pad = 10, backgroundcolor = 'lightgray')

# 슈퍼 타이틀 설정
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 1, 2, 1]

plt.subplot(2, 1, 1)
plt.plot(x, y1)
plt.title('Graph Sub Title 1', loc = 'left')

plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.title('Graph Sub Title 2', loc = 'left')

plt.suptitle('Gragh Super Title')
plt.tight_layout()
plt.show()

