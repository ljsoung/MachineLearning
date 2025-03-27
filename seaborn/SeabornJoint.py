# 조인트 그래프

import seaborn as sns

# 맷플롭립 라이브러리 불러오기
import matplotlib.pyplot as plt

# 팁 데이터셋 불러오기
tips = sns.load_dataset("tips")

#jointplot()
sns.jointplot(x='size', y='tip', data=tips, kind='scatter')
plt.show()
