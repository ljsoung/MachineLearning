# 시본 라이브러리 불러오기
import seaborn as sns

# 시본 내장 데이터의 종류출력
# print(sns.get_dataset_names())

# 팁 데이터 셋을 불러온 다음, 데이터 셋의 구성을 살펴보기
tips = sns.load_dataset("tips")
# print(tips.head())

# info( ) : 열에 대한 요약 정보 확인
# 행과 열의 크기, 컬럼명, 컬럼별 결측치, 컬럼별 데이터 타입
# print(tips.info())

# 맷플롯립 라이브러리 불러오기
import matplotlib.pyplot as plt

# 팀 데이터셋 불러오기
tips = sns.load_dataset("tips")

#figure에 2개의 서브 플롯을 생성
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

#stripplot() 그리기
sns.stripplot(x = 'day', y = 'tip', hue = 'sex', data = tips, alpha = 0.7, ax = ax1)

#swarmplot() 그리기
sns.swarmplot(x = 'day', y = 'tip', hue = 'sex', data = tips, palette = 'Set2', alpha = 0.7, ax = ax2)

# 서브 플롯의 제목 설정
ax1.set_title('Strip Plot of Tip by Day and Gender')
ax2.set_title('Swarm Plot of Tip by Day and Gender')
plt.show()