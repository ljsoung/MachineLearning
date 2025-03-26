import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4], [3, 6, 9, 12])

# plt.xlim([0, 5])
# plt.ylim(0, 15)

# x, y축 둘 다 범위를 지정하고 싶을 때는 axis()
plt.axis([0, 5, 0, 15])
plt.show()