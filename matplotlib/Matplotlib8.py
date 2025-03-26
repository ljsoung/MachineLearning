import matplotlib.pyplot as plt
x = [1, 2, 3] # x 정의
years = ['2030', '2040', '2050'] # x축에 표시할 연도
values = [300, 100, 700] # y축에 표시할 값

# 막대 그래프 생성, 색상 설정은 color 매개변수로 설정
plt.bar(x, values, color = ['red', 'green', 'blue'])

# x축 눈금에 '2030', '2040', '2050'를 표시
plt.xticks(x, years)
plt.show()

