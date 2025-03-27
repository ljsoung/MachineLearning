# Matplotlib - 파이썬으로 그래프를 그리는 다양한 기능 제공
# 그래프의 범례, 축 범위 설정과 같이 다양한 시각화 설정 옵션 제공

# 데이터 시각화 하면 좋은 점
# 1. 데이터의 패턴이나 상관관계를 시각적으로 쉽게 이해
# 2. 데이터의 분포, 이상치, 결측치 등을 빠르게 파악

# Matplotlib을 이용한 시각화의 장점
# 1. 다양한 플롯 타입: 라인, 바, 히스티그램, 스캐터 등
# 2. 높은 커스터마이징: 레이블, 축, 색상 등 세밀한 제어 옵션 제공
# 3. 통합성: 다른 분석도구와 잘 통합
# 4. 광범위한 사용자 커뮤니티와 문서
# 5. 다양한 출력 포멧: PNG, PDF, SVG 등을 지원
# 6. 애니메이션 지원: 시간에 따라 변화하는 데이터 시각화
# 7. Ipython 및 Jupyter 노트북과의 호환성

import matplotlib.pyplot as plt

# 하나의 숫자 리스트 입력
y = [2, 3, 4, 5]
# plt.plot(y)
# plt.show()

# 첫 번째 리스트의 값은 x값, 두 번째 리스트의 값은 y로 적용
# 순서쌍 (x, y)으로 매칭된 값을 좌표평면 위에 그래프 시각화
# plt.plot([1, 2], [2, 4])
# plt.show()

# 두 개의 숫자 리스트 입력하여 그래프 그리기
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# xlabel() 함수에 'X-Label' 입력하여 x축에 대한 레이블 표시
# plt.xlabel('X-Label')
# plt.ylabel('Y-Label')
# plt.show()

# plot() 함수의 label 매개변수에 'Square' 문자열 입력
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], label = 'Square')
# plt.xlabel('X-Label')
# plt.ylabel('Y-Label')

#legend() 함수를 사용해서 그래프에 범례 표시
# plt.legend()
# plt.show()

import numpy as np
x = np.linspace(0, 10, 100)
y1 = x
y2 = 2 * x
y3 = 0.5 * x
y4 = 3 * x

plt.plot(x, y1, label = 'y = x')
plt.plot(x, y2, label = 'y = 2x')
plt.plot(x, y3, label = 'y = 0.5x')
plt.plot(x, y4, label = 'y = 3x')

# 범례 설정(ncol을 2로 설정하여 한 줄에 2개 표시)
plt.legend(loc = 'upper center', ncol = 3)

# 타이틀 및 축 라벨 설정
plt.title('Simple Linear Plot Example')
plt.xlabel('x')
plt.ylabel('y')
plt.show()