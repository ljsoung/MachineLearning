# K-최근접 이웃(KNN)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/wine.csv'
data = pd.read_csv(file_url)

# print(data.head())

# print(data['class'].unique()) # 목표 변수의 고윳값 출력
# print(data['class'].nunique()) # 고윳값 가짓수 출력
# print(data['class'].value_counts()) # 각 고윳값에 해당하는 개수 출력

# 막대 그래프로 고윳값 시각화하기
# sns.barplot(x = data['class'].value_counts().index, y = data['class'].value_counts())
# plt.show()

# sns의 countplot()을 활용하여 시각화하기 -> 좀 더 간편
# sns.countplot(x = 'class', data = data)
# plt.show()

### 전처리: 결측치 처리하기

# 결측치를 쉽게 확인하는 방법
# print(data.isna()) # 값을 결측치 여부에 따라 True, False로 반환
# print(data.isna().sum()) # 결측치 수만큼 더한 값 반환
# print(data.isna().mean()) # 결측치 값의 평균 반환

# 결측치를 처리하는 방법

# 결측치 행 제거하기: dropna()
# print(data.dropna()) # 결측치가 있는 행 제거
#print(data.dropna().isna().mean()) # 결측치 제거 확인하기

# print(data.dropna(subset=['alcohol'])) # alcohol에서 결측치 제거
# print(data.dropna(subset=['alcohol']).isna().mean()) # alcohol의 결측치 제거 후 평균 반환

# 결측 변수 제거하기: drop()
# print(data.drop(['alcohol', 'nonflavanoid_phenols'], axis=1)) # alcohol과 nonflavanoid_phenols 열 제거

# 결측값 채우기: fillna()
# print(data.fillna(-99)) # 결측치를 -99로 채우기
# print(data.fillna(data.mean()).round(2)) # 각 컬럼의 평균값으로 결측치 채우기

data.fillna(data.median(), inplace=True) # 결측치를 중윗값으로 채우기 -> 이게 좋음
# print(data.isna().mean())

# 스케일링
# Standard Scaler
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
st_scaler = StandardScaler() # 표준화 스케일링
st_scaler.fit(data) # 학습
st_scaled = st_scaler.transform(data) # 학습에서 얻은 정보 계산
st_scaled = pd.DataFrame(st_scaled, columns=data.columns)
# print(st_scaled)

# Robust Scaler
rb_scaler = RobustScaler() # 로버스트 스케일링
rb_scaled = rb_scaler.fit_transform(data) # 학습과 변환을 동시에
rb_scaled = pd.DataFrame(rb_scaled, columns = data.columns)
# print(rb_scaled.describe().round(2))

#MinMax Scaler
mm_scaler = MinMaxScaler() # 최소최대 스케일링
mm_scaled = mm_scaler.fit_transform(data) # 학습과 변환을 동시에
mm_scaled = pd.DataFrame(mm_scaled, columns=data.columns)
# print(round(mm_scaled.describe(), 2))

# 스케일링 적용하기
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data.drop(['class'], axis = 1), data['class'], test_size = 0.2, random_state = 100)
mm_scaler = MinMaxScaler()
X_train_scaled = mm_scaler.fit_transform(X_train) # 학습과 변환
X_test_scaled = mm_scaler.transform(X_test) # 이미 학습되었으므로 변환만

### 모델링 및 예측/평가하기
# 예측하기
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 6)
knn.fit(X_train_scaled, y_train)
pred = knn.predict(X_test_scaled)
# print(pred)

# 예측하기 (하이퍼파라미터)
from sklearn.metrics import accuracy_score
scores = []
for i in range(1, 21):
  knn = KNeighborsClassifier(n_neighbors=i)
  knn.fit(X_train_scaled, y_train)
  pred = knn.predict(X_test_scaled)
  acc = accuracy_score(y_test, pred)
  scores.append(acc)
  # print(acc)

# 시각화하기
sns.lineplot(x = range(1, 21), y = scores)
# plt.show()

knn = KNeighborsClassifier(n_neighbors=13)
knn.fit(X_train_scaled, y_train)
pred = knn.predict(X_test_scaled)
print(accuracy_score(y_test, pred))