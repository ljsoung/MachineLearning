import pandas as pd

# 타이타닉 CSV 파일 불러오기
titanic = pd.read_csv('3.1.1.titanic.csv')

#데이터 처음 5개의 행 출력
# titanic.head()

# 열에 대한 요약 정보 확인
# titanic.info()

# 객실 등급에 따른 생존자와 사망자의 평균 계산
pclass_survived_mean = titanic.groupby('Pclass')['Survived'].mean().reset_index()
# print(pclass_survived_mean)

import matplotlib.pyplot as plt
plt.plot(pclass_survived_mean['Pclass'], pclass_survived_mean['Survived'], marker = 'o', linestyle = '-', color = 'violet')
plt.title('Survival Rate Variation Across Passenger Classes')
plt.xlabel('Pclass')
plt.ylabel('Survival Rate')
plt.xticks([1, 2, 3])
plt.grid(True)
# plt.show()

# 승선 항구에 따른 생존자 수 계산
survived_counts = titanic[titanic['Survived'] == 1]['Embarked'].value_counts()
print(survived_counts)

# 막대 그래프 그리기
plt.bar(survived_counts.index, survived_counts, color = ['mediumorchid', 'darkviolet', 'indigo'])
plt.title('Survived Counts by Embarked Port on Titanic')
plt.xlabel('Embarked Port')
plt.ylabel('Count')
plt.xticks(survived_counts.index, ['Southampton', 'Cherbourg', 'Queenstown'])
plt.legend(['Survived'], loc = 'upper right')

# 생존자 수 표시
for i, value in enumerate(survived_counts):
    plt.text(i, value + 1, str(value), ha = 'center', va = 'bottom')

# plt.show()

bars = plt.barh(survived_counts.index, survived_counts, color = ['darkturquoise', 'salmon'])
plt.title('Survived Counts by Gender on Titanic')
plt.xlabel('Count')
plt.ylabel('Gender')
plt.legend(bars, ['Survived - Female', 'Survived - Male'], loc = 'upper right')

# 차이 강조를 위해 수평선 추가
plt.axvline(x = survived_counts['male'], color = 'gray', linestyle = '--', linewidth = 1)

# 생존자 수 표시
for i, value in enumerate(survived_counts):
    plt.text(i, value + 1, str(value), ha = 'left', va = 'center')