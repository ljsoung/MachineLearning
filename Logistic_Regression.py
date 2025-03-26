import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/titanic.csv'
data = pd.read_csv(file_url)

# print(data.head())
# print(data.info())
# print(data.describe())

# 상관관계를 위해 문자열로 되어 있는 데이터는 삭제
num_data = data.drop(['Name', 'Sex', 'Ticket', 'Embarked'], axis=1)
# print(num_data.corr()) # 상관관계 출력

# 데이터 시각화 하기
import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(num_data.corr()) # 상관관계에 대한 히트맵 생성
# plt.show()

# 밝은 톤으로 히트맵 생성
sns.heatmap(num_data.corr(), cmap = 'coolwarm')
# plt.show()

# 최소값 : -1, 최대
sns.heatmap(num_data.corr(), vmin = -1, vmax = 1, annot=True)
# plt.show()
data = data.drop(['Name', 'Ticket'], axis=1) # 불필요한 Name, Ticket 컬럼 삭제
# print(data.head())

#남은 두 object형을 원-핫 인코딩
# print(pd.get_dummies(data, columns=['Sex', 'Embarked']))

#더미 변수 하나를 줄여서 데이터 계산량 줄이기
data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)
# print(data.head())

from sklearn.model_selection import train_test_split
X = data.drop('Survived', axis=1) # 데이터셋에서 종속변수 제거 후 저장
y = data['Survived'] # 데이터셋에서 종속변수만 저장

# 학습셋, 시험셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

from sklearn.model_selection import train_test_split # 로지스틱 회귀 임포트
model = LogisticRegression() # 로지스틱 회귀 모델 생성
model.fit(X_train, y_train) # 모델 학습
pred = model.predict(X_test) # 예측

print(accuracy_score(y_test, pred))

# model.coef_를 7개 값이 되도록 풀어서 컬럼 이름 매핑
# print(pd.Series(model.coef_[0], index = X.columns))

data['family'] = data['SibSp'] + data['Parch'] # SibSp와 Parch 변수 합치기
data.drop(['SibSp', 'Parch'], axis=1, inplace=True) # SibSp와 Parch 변수 삭제
# print(data.head()) # 5행 출력


