import matplotlib.pyplot as plt
# 뒷 배경 라인 설정(grid)
# plt.plot([1, 2, 3, 4], [10 , 5, 10, 5])

#그리드 활성화 및 설정
# plt.grid(True, linestyle = '--', linewidth = 0.5, color = 'black', alpha = 0.7)

categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 20]

# 막대 그래프 생성
plt.bar(categories, values, color = 'skyblue')

for i, v in enumerate(values):
    plt.text(i, v + 0.1, str(v), ha = 'center', va = 'bottom', color = 'black', fontsize = 12)

plt.title('Bar Chart with Text Annotations')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()
