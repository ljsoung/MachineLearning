# 범주형 변수 산점도 그래프

import seaborn as sns

# 맷플롭립 라이브러리 불러오기
import matplotlib.pyplot as plt

# 팁 데이터셋 불러오기
tips = sns.load_dataset("tips")

# figure에 2개의 서브 프롯을 생성 .add_subplot()
fig = plt.figure(figsize = (15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# stripplot() 그리기 -> 연속형 변수와 연속형 변수의 관계
sns.stripplot(x = 'day', y = 'tip', hue='sex', data = tips, alpha = 0.7, ax = ax1)

# swarmplot() 그리기 -> 범주형 변수와 연속현 변수의 관계
sns.swarmplot(x = 'day', y = 'tip', hue='sex', data = tips, palette = 'Set2', alpha = 0.7, ax = ax2)

# 서브 플롯의 제목 설정
ax1.set_xlabel('Strip Plot of Tip by Day and Gender')
ax2.set_xlabel('Swarm Plot of Tip by Day and Gender')
plt.show()

