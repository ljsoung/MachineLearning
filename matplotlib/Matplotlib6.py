import matplotlib.pyplot as plt

# 이름으로 색상 설정(예 : 'violet')
plt.plot([1, 2, 3, 4], [2.0, 3.3, 6.3, 10.5], color = 'violet')

# 약자로 색상 설정 (예:'g')
plt.plot([1, 2, 3, 4], [2.0, 3.1, 5.3, 8.5], color = 'g')

# RGB 값으로 색상 설정
plt.plot([1, 2, 3, 4], [2.0, 2.8, 4.3, 6.5], color = (0.1, 0.2, 0.3))

# 16진수로 색상 설정
plt.plot([1, 2, 3, 4], [2.0, 2.5, 3.3, 4.5], color = '#FF0000')

plt.show()
