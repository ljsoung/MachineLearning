import matplotlib.pyplot as plt
import numpy as np

#plot() 함수의 세 번째 인수 값으로 간략화한 문자열을 입력하여 선 종류 선택
plt.plot([1, 2, 3], [4, 4, 4], '-', label = 'solid')
plt.plot([1, 2, 3], [3, 3, 3], '--', label = 'dashed')

#plot() 함수의 linestyle 값으로 문자열을 입력하여 선 종류 설정
plt.plot([1, 2, 3], [2, 2, 2], linestyle = 'dotted', label = 'dotted')
plt.plot([1, 2, 3], [1, 1, 1], linestyle = 'dashdot', label = 'dashdot')

plt.axis([0.8, 3.2, 0.5, 5.0])
plt.legend(loc = 'upper center', ncol = 4)
plt.show()

#선의 종류는 vo.la/NsmLBW 에서 확인


