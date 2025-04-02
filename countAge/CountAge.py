import pandas as pd

age_df = pd.read_csv('3.3.1.age.csv', encoding='cp949', low_memory=False)

# 컬럼명에서 '2025년 02월_' 지우기
age_df.columns = age_df.columns.str.replace('2025년02월_', '')

# print(age_df.head())

# 행정구역이 '불당1동'인 구역 검색
filtered_df = age_df[age_df['행정구역'].str.contains('불당1동', na=False)]

# print(filtered_df.head())

result = filtered_df.iloc[0, 3:104].astype(int).values.tolist()

print(result)

# 맵플롭립으로 데이터 시각화
import matplotlib.pyplot as plt
plt.plot(result)
plt.show()