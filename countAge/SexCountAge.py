# 성별에 따른 인구 데이터 추출하기

import pandas as pd

age_df = pd.read_csv('3.3.1.age.csv', encoding='cp949', low_memory=False)
age_df.columns = age_df.columns.str.replace('2025년02월_', '')

# 사용자로부터 원하는 지역 입력 받기
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')

filtered_df = age_df[age_df['행정구역'].str.contains(name, na=False)]

male_result = filtered_df.iloc[0,106:207]
female_result = filtered_df.iloc[0,209:310]

# print(male_result)
# print(female_result)

# 데이터 변환
male_result = [int(value) for value in male_result]
# print(male_result)

female_result = [int(value) for value in female_result]
# print(female_result)

# 데이터 시각화하기
import matplotlib.pyplot as plt
# plt.barh(range(len(male_result)), male_result, label='male')
# plt.barh(range(len(female_result)), female_result, label='female')
# plt.legend()

# 남성 데이터를 음수로 바꾸기
male_result = [-value for value in male_result]

# 다시 수평바 그래프 그리기
plt.barh(range(len(male_result)), male_result, label='male')
plt.barh(range(len(female_result)), female_result, label='female')
plt.legend()
plt.show()