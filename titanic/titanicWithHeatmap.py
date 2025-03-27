import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv('3.1.1.titanic.csv')
titanic = titanic.dropna(subset=['Age', 'Fare']) # 결측치 처리

# 상관 행렬 계산
correlation_matrix = titanic.drop('PassengerId', axis = 1).corr(numeric_only=True)
print(correlation_matrix)

plt.matshow(correlation_matrix, cmap='PuRd_r')
plt.colorbar() # 오른쪽에 색상 참고를 위한 컬러바 추가

# x축과 y축의 눈금 설정
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title('Correlation Heatmap of Titanic')
plt.show()
