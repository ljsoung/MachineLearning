# 션형 회귀선 있는 산점도 그래프

import seaborn as sns

# 맷플롭립 라이브러리 불러오기
import matplotlib.pyplot as plt

# 팁 데이터셋 불러오기
tips = sns.load_dataset("tips")

# 히스토그램과 커널 밀도 추정 그래프 함께 그리기
sns.histplot(tips['tip'], bins=30, kde=True, color='skyblue')

# 제목 설정
plt.title('Histogram with KDE for Tips')
plt.show()

