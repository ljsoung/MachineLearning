import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv('3.1.1.titanic.csv')
titanic = titanic.dropna(subset=['Age']) # 나이 결측치 처리

# 히스토그램: 승객의 나이 분포 표시
plt.figure(figsize=(10,6))
plt.hist(titanic['Age'], bins = 20, color = 'seagreen', edgecolor = 'black')

plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Distribution of Ages on the Titanic')
plt.grid(axis='y', linestyle='--', alpha=0.7) # 그래프에 격자선 추가
# plt.show()