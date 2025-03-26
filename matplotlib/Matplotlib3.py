# 스케일 지정
import matplotlib.pyplot as plt
import numpy as np

#데이터 생성
x = np.linspace(0, 10, 100)
y = np.exp(x) # 지수함수 (e^x)

# 선형 스케일 - 축에 일정 간격으로 눈금을 표시
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('Linear Scale')

# 로그 스케일 - 값의 크기 차이가 큰 경우
plt.subplot(2, 2, 2)
plt.plot(x, y)
plt.yscale('log')
plt.title('Logarithmic Scale(y-axis)')

# 로그-선형 스케일 - x축이 시간이나 크기를 나타낼 때
plt.subplot(2, 2, 3)
plt.plot(x, y)
plt.xscale('log')
plt.title('Logarithmic Scale(y-axis)')

# 선형-로그 스케일 - 주로 y축의 값 범위가 큰 경우
plt.subplot(2, 2, 4)
plt.plot(x, y)
plt.xscale('linear')
plt.yscale('log')
plt.title('Linear - Logarithmic Scale(y-axis)')

plt.tight_layout() # 서브 그래프 간격 조절
plt.show()