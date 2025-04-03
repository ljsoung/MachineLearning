# 나이브 베이즈 알고리즘
# 조건부 확률 -> A가 일어나면 B가 일어날 확률(A가 일어나야 함)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/spam.csv'
data = pd.read_csv(file_url)

import string

# print(string.punctuation)

# 샘플 문자열 하나 가져오기
sample_string = data['text'].loc[0]
# print(sample_string)

# 문자열의 문자를 하나씩 출력
# for i in sample_string:
#     print(i)

# 특수기호가 아닌 문자열만 보이게 하기
# for i in sample_string:
#    if i not in string.punctuation:
#         print(i)

# 특수 기호를 제외한 문자들을 리스트에 모아주기
new_string = []
for i in sample_string:
    if i not in string.punctuation:
        new_string.append(i)
# print(new_string)

# 리스트 안의 문자들을 문자열로 만들기
new_string = ''.join(new_string)


# print(new_string)


def remove_punc(x):
    global new_string, i
    # 특수 기호를 제외한 문자들을 리스트에 모아주기
    new_string = []
    for i in x:
        if i not in string.punctuation:
            new_string.append(i)
    # print(new_string)
    # 리스트 안의 문자들을 문자열로 만들기
    new_string = ''.join(new_string)
    return new_string


# text 컬럼의 한 행마다 특수기호 제거하기
data['text'] = data['text'].apply(remove_punc)
# print(data['text'])

# nltk 라이브러리에서 불용어 목록 가져오기
import nltk
# nltk.download('stopwords')

# stopword 임포트 하기
from nltk.corpus import stopwords

# stopword에서 제공하는 리스트 확인
# print(stopwords.words('english'))

# 단어 단위로 문장 분할
sample_string = data['text'][0]
# print(sample_string.split())

# 각 단어가 불용어에 속하는지 아닌지 판독
# for i in sample_string.split():
#     if i.lower() not in stopwords.words('english'):
#         print(i.lower())


# 불용어 제거 함수
def stop_words(x):
    new_string = []
    for i in x.split():
        if i.lower() not in stopwords.words('english'):
            new_string.append(i.lower())
    new_string = ' '.join(new_string)

    return new_string

# data['text'] = data['text'].apply(stop_words)
# print(data['text'])

# 전처리: 목표 컬럼 형태 변경하기
data['target'] = data['target'].map({'spam':1, 'ham':0})
# print(data['target'])

x = data['text'] # 독립 변수
y = data['target'] # 종속 변수

# CounterVectorizer 임포트
from sklearn.feature_extraction.text import CountVectorizer

# 학습하기 (단어와 인덱스 생성)
cv = CountVectorizer()
cv.fit(x)
# print(cv.vocabulary_)

# 변환하기 (문장 벡터화하기)
x = cv.transform(x)
print(x)