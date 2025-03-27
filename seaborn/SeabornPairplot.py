# 관계 그래프

import seaborn as sns

# 맷플롭립 라이브러리 불러오기
import matplotlib.pyplot as plt

# 팁 데이터셋 불러오기
tips = sns.load_dataset("tips")

# pairplot() 그리기
sns.pairplot(data=tips, hue='sex', diag_kind='hist', palette='husl')

# 제목 설정
plt.suptitle('Pairplot with Histograms by Gender', y=1.05)
plt.show()