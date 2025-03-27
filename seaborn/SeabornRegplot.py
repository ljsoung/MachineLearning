# 션형 회귀선 있는 산점도 그래프

import seaborn as sns

# 맷플롭립 라이브러리 불러오기
import matplotlib.pyplot as plt

# 팁 데이터셋 불러오기
tips = sns.load_dataset("tips")

# figure에 2개의 서브 프롯을 생성 .add_subplot()
fig = plt.figure(figsize = (15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# 산점도에 선형 회귀선 표시(fit_reg=True) -> default
sns.regplot(x='total_bill', y='tip', data=tips, color='blue', scatter_kws={'s': 50, 'alpha': 0.5}, line_kws={'linestyle': '--'}, ax=ax1)

# 산점도에 선형 회귀선 미표시(fit_reg=False)
sns.regplot(x='total_bill', y='tip', data=tips, color='red', scatter_kws={'s':50, 'alpha': 0.5}, line_kws={'linestyle': '--'}, ax=ax2, fit_reg=False)

# 제목 설정
fig.suptitle('Scatter Plots with Regression Lines', fontsize=16)
ax1.set_title('fit_reg = True')
ax2.set_title('fit_reg = False')
plt.show()