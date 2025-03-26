import pandas as pd
file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/sample.csv'
sample = pd.read_csv(file_url) # .read_csv csv파일을 판다스에서 데이터 프레임 형태로 불러온다.
# print(sample)
# print(sample.head())
# print(sample.tail())
# print(sample.info())
# print(sample.describe())

#데이터 프레임 직접 만들기
sample_dic = {'name': ['John', 'Ann', 'Kevin'],
              'age': [23, 22, 21]}
# print(pd.DataFrame(sample_dic))
# print(pd.DataFrame([[1,2],[3,4],[5,6],[7,8]])) # 리스트 안에 리스트 구조로 넣어야 함
# print(pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns = ['var_1','var_2'], index = ['a', 'b', 'c', 'd']))

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/sample_df.csv'
sample_df = pd.read_csv(file_url, index_col = 0) # 첫 번째 열을 인덱스로 설정
# print(sample_df.head())
# print(sample_df['var_1'])
# print(sample_df[['var_1', 'var_2']])

# print(sample_df.loc['a':'c'])
# print(sample_df.iloc[0:3, 2:4])
# print(sample_df['var_1'].isin([4])) # 값이 4가 들어 있는 부분을 True로 리턴
sample_df.drop('var_1', axis=1)
# print(sample_df.drop(['var_1', 'var_2'], axis = 1))
# print(sample_df.drop(['a', 'b', 'c'], axis = 0))

netflix = pd.read_csv('2.1.1.netflix.csv')
# print(netflix.head())
# more2015 = netflix[netflix['release_year'] > 2015]
# more2015 = netflix[~(netflix['release_year'] > 2015)]
more2015_tv = netflix[(netflix['release_year'] > 2015) | (netflix['type'] == 'TV Show')] # 괄호 꼭 해줘야 함
# print(more2015_tv.head())

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'comment_length': [150, 200, 50, 300, 120, 180, 75, 160],
    'likes': [25, 30, 10, 45, 20, 35, 5, 28],
    'is_spam': [False, False, True, False, False, True, False, False],
    'has_image': [True, False, True, True, False, False, True, True]
}
df = pd.DataFrame(data)
# print(df)

# 필터링 조건 설정
condition = (
  (df['comment_length'] >= 100) &       # 댓글 길이 100자 이상
  (df['likes'] >= 20) &                 # 좋아요 20개 이상
  (~df['is_spam']) &                    # 스팸 댓글이 아니어야 함
  (df['has_image'])                     # 이미지가 포함된 댓글이어야 함
)

# 조건을 만족하는 행들 필터링
winner_df = df[condition]
# print(winner_df)

# test = sample_df.reset_index() # 기존 인덱스 제거 후 default값 지정 -> 기존 인덱스가 값으로 들어가버림. 데이터 분석 시 곤란해짐
test = sample_df.reset_index(drop=True) # 기존 인덱스를 완전 제거
# print(test.head())

# print(sample_df.sum())
# print(sample_df.aggregate(['sum', 'mean']))

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/iris.csv'
iris = pd.read_csv(file_url)
# print(iris.head())
# print(iris.groupby('class').mean())
# print(iris.groupby('class').agg(['sum', 'mean']))
# print(iris['class'].unique())
# print(iris['class'].nunique())
#print(iris['class'].value_counts())

# 예제 데이터 생성
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 40],
    'salary': [70000.00, 80000.00, 90000.00, 60000.00, 95000.00]
}

# Dataframe 생성
df = pd.DataFrame(data)
# print(df.head())

# 나이가 30 이상인 직원의 이름과 급여 반환

result = df[df['age'] >= 30][['name', 'salary']]
# print(result)

# 예제 데이터 생성
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'math': [88, 92, 85, 95, 90],
    'science': [80, 85, 88, 92, 85],
    'english': [90, 87, 85, 88, 92]
}

# Dataframe 생성
df = pd.DataFrame(data)

# 개인별 과목 점수의 평균값 계산 (axis=1)
# 개인별 과목 점수의 평균값 계산 (axis=1)
df['average'] = df[['math', 'science', 'english']].mean(axis=1)

# 이름과 평균값만을 포함하는 새로운 데이터프레임 생성
average_df = df[['name', 'average']]

# print(average_df)

import numpy as np
# print(np.array([1, 2, 3]))

# print(np.array([[1,2,3], #2차원 배열
#                [4,5,6],
#                [7,8,9]]))

# print(np.array([[[1,2,3], #3차원 배열
#           [4,5,6],
#           [7,8,9]],
#          [[1,2,3],
#           [4,5,6],
#           [7,8,9]],
#          [[1,2,3],
#           [4,5,6],
#           [7,8,9]]]))

# print(np.array(sample_df))
sample_np = np.array(sample_df)
# print(pd.DataFrame(sample_np))
# print(sample_df.columns)
#print(pd.DataFrame(sample_np, index= sample_df.index ,columns=sample_df.columns))

# print(sample_np[0])

print(sample_np[0, 2])