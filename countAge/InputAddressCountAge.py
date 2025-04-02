# 동을 입력받아 그래프 그리기
import pandas as pd

age_df = pd.read_csv('3.3.1.age.csv', encoding='cp949', low_memory=False)
age_df.columns = age_df.columns.str.replace('2025년02월_', '')

# 사용자로부터 원하는 지역 입력 받기
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')

filtered_df = age_df[age_df['행정구역'].str.contains(name, na=False)]
result = filtered_df.iloc[0,3:104].astype(int).values.tolist()

import matplotlib.pyplot as plt
plt.plot(result)
plt.show()