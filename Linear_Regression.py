import pandas as pd
from sklearn.metrics import mean_squared_error

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/insurance.csv'
data = pd.read_csv(file_url)

#전처리
X = data[['age', 'sex', 'bmi', 'children', 'smoker']]
y = data['charges']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# 모델링
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train) # 학습 시키는겨

pred = model.predict(X_test)
# print(pred)

comparison = pd.DataFrame({'actual': y_test, 'pred': pred})
#print(comparison)

# 예측 결과를 시각적으로 평가
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 10))
sns.scatterplot(x = 'actual', y = 'pred', data = comparison)
plt.show()

#모델 성능 수치 평가하기
from sklearn.linear_model import LinearRegression
mse = mean_squared_error(y_test, pred) ** 0.5

