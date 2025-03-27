# 빈도 그래프

import seaborn as sns

# 맷플롭립 라이브러리 불러오기
import matplotlib.pyplot as plt

# 팁 데이터셋 불러오기
tips = sns.load_dataset("tips")

# figure에 2개의 서브 플롯을 생성
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# 식사가 이루어진 시간대 파악
# x축 변수, 데이터셋, axe 객체(1번째 그래프)
sns.countplot(x = 'time', data = tips, ax = ax1)

# 식사가 이루어진 시간대 파악과 식사가 이루어진 요일로 색상 분류
# x축 변수, hue로 색상 분류, 데이터 셋, 색상 설정, axe 객체(2번째 그래프)
sns.countplot(x = 'time', hue = 'day', data = tips, palette='Set2', ax = ax2)

#서브 플롯의 제목 설정
ax1.set_title('Frequency of Tips by Time')
ax2.set_title('Frequency of Tips by Time and Day')
plt.show()