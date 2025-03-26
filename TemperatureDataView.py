import random
dice = []

for i in range(5):
    dice.append(random.randint(1,6))

print(dice)

import matplotlib.pyplot as plt
# plt.hist(dice, bin = 6)
# plt.show()

# 기온 데이터를 히스토그램으로 표현하기
import pandas as pd

data = pd.read_csv('3.1.2.temp.csv', encoding='cp949')
data['날짜'] = data['날짜'].str.replace('\t', '')
data['날짜'] = pd.to_datetime(data['날짜'])

result = data.iloc[:, [0,4]]

# plt.hist(result['최고기온(℃)'], bins=100, color='r')
# plt.show()

# 월별로 최고 기온을 박스플롯으로 표현하기
data = pd.read_csv('3.1.2.temp.csv', encoding='cp949')
data['날짜'] = data['날짜'].str.replace('\t', '')
data['날짜'] = pd.to_datetime(data['날짜'])

result = data.iloc[:, [0,4]]

monthly_temp = []
for month in range(1, 13):
  monthly_temp.append(list(result[result['날짜'].dt.month == month]['최고기온(℃)']))

print (monthly_temp)

plt.boxplot(monthly_temp)
plt.show()