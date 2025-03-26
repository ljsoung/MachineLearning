# 폰트 설정 코드
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
    font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows의 기본 한글 폰트
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)
else:
    # macOS의 경우 예시
    rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지



import pandas as pd

data = pd.read_csv('3.1.temp.csv', encoding='cp949')
# print(data.head())

# 날짜 앞의 \t 없애기
data['날짜'] = data['날짜'].str.replace('\t', '')
# print(data.head())

# 날짜 컬럼의 object 타입을 날짜형식(datetime)으로 변환하기
data['날짜'] = pd.to_datetime(data['날짜'])
# print(data.info())

# 최고 기온만 날짜와 함께 저장하기
result = data.iloc[:, [0, 4]]
# print(result)

# 데이터 시각화 하기
import matplotlib.pyplot as plt
# plt.plot(result['최고기온(℃)'])
# plt.show()

# 내가 태어난 달에 해당하는 온도만 추출
birthday_result = result[(result['날짜'].dt.month == 9) & (result['날짜'].dt.day == 23)]
# print(birthday_result)

# plt.plot(birthday_result['최고기온(℃)'])   # x축 날짜는 생략
# plt.show()

# 내 생일의 최저 기온과 최고 기온을 모두 추출하기
birthday_result2 = data[(data['날짜'].dt.month == 9) & (data['날짜'].dt.day == 16)]
# plt.plot(birthday_result2['최저기온(℃)'])
# plt.plot(birthday_result2['최고기온(℃)'])
# plt.show()

plt.plot(birthday_result2['날짜'], birthday_result2['최저기온(℃)'])
plt.plot(birthday_result2['날짜'], birthday_result2['최고기온(℃)'])
plt.title('내 생일의 기온 변화 그래프')
plt.show()