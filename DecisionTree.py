import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/salary.csv'
# skipInitialSpace: 각 데이터의 첫 자리에 있는 공란 자동 제거
data = pd.read_csv(file_url, skipinitialspace = True)

# class 고윳값 및 특징 확인하기
# print(data['class'].unique())
# print(data.info())

# 전처리: 범주형 데이터
# 종속 변수 class 처리
data['class'] = data['class'].map({'<=50K': 0, '>50K': 1})
# object형 변수를 따로 리스트에 저장
obj_list = []
for i in data.columns:
    if data[i].dtype == 'object':
        obj_list.append(i)

# print(obj_list)

# 각 변수의 고윳값 개수 확인
# for i in obj_list:
#     print(i, data[i].nunique())

# education과 education-num 변수
# for i in np.sort(data['education-num'].unique()):
#    print(i, data[data['education-num']==i]['education'].unique())
# 슷자가 커질수록, 고학력을 뜻함 -> 서열을 가진 변수

# education 변수는 제거
data.drop('education', axis = 1, inplace = True)

# 이미 비슷한 직업군끼리 묶인 상태
# 직업간 서열이라고 할만한 부분 없음
# 모두 더미 변수로 변환해야 함 (14개)
# print(data['occupation'].value_counts())

# 나라별 class 평균값 확인
# 미국과 다른 나라들의 class 평균값 차이가 큼
# 같은 유럽(Frnace, Portual) 끼리도 class 평균 차이가 큼
# 지역별 유사성이 없으므로 지역으로 묶는 것은 부적합
# print(data.groupby('native-country').mean(numeric_only=True).sort_values('class'))

# 국가명을 숫자로 변환 시 서열이 없는 범주형 데이터를 숫자로 치환(X)
# 그러나 트리 기반 모델은 연속된 숫자도 숫자가 아닌 일정 구간으로
# 나누어 받아들이기 때문에 문제 없음

# 국가명을 숫자로 변환하는 방법
# 국가별로 랜덤하게 번호 부여
# value_counts()함수의 결과를 보고 번호로 부여 -> 중복 가능성이 있음
# ★ groupby('class').mean() 결과를 번호로 부여하는 것이 정확

# natove-country(범주형)를 국가별 class 평균(숫자)로 치환
data['native-country'] = data['native-country'].map(
    data.groupby('native-country')['class'].mean()
)
# print(data)

# 결측치 처리 및 더미 변수 변환
# workclass, occupation, native-country에 결측치가 존재

# native-country 결측치 처리
# 선형 모델은 mean(), median() 등으로 결측치를 채우지만
# 트리 기반 모델은 -9, -99 등의 임의 숫자 사용
# 선형 모델에서는 데이터가 왜곡되므로 사용하지 않음
data['native-country'] = data['native-country'].fillna(-99)

# workclass (범주형) 결측치 처리
# value_counts()로 고윳값 출현 빈도 확인
# 빈도수가 가장 높은 값을 결측치에 대체 값으로 사용
# print(data['workclass'].value_counts())
data['workclass'] = data['workclass'].fillna('Private')

#occupation (범주형) 결측치 처리
# value_counts()로 고윳값 출현 빈도 확인
# 특정 값이 압도적으로 많다고 하기 어려운 경우
# 'Unknown'으로 대체
data['occupation'] = data['occupation'].fillna('Unknown')

# 나머지 범주형 변수를 더미 변수로 변환
data = pd.get_dummies(data, drop_first = True)

# 훈련셋과 시험셋 나누기
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data.drop('class', axis = 1), data['class'], test_size = 0.4, random_state = 100)

# 결정트리 모델 선택하기
from sklearn.tree import DecisionTreeClassifier

# 모델링 및 예측 하기
# 트리 깊이가 깊어지면 -> 오버 피팅 발생
# 트리의 깊이를 제한하여 오버피팅 해결
# max_depth 활용
model = DecisionTreeClassifier(max_depth = 7)
model.fit(X_train, y_train)
pred = model.predict(X_test)

# 정확도 확인하기
from sklearn.metrics import accuracy_score
accuracy_score(y_test, pred)

from sklearn.tree import plot_tree
plt.figure(figsize = (30, 15))
plot_tree(model, max_depth = 3, fontsize = 15, feature_names=X_train.columns)