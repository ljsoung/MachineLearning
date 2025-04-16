# URL을 통해 데이터를 받을 수 있는 requests 패키지 import
import requests
import pandas as pd

# API 호출 URL 설정
url = "http://data4library.kr/api/loanItemSrch?authKey=756dbdc8712de77e5ff3667c0e0ba0b9ce10bf2d2ffd5d4481f32226b728aa37&startDt=2021-04-01&endDt=2021-04-30&age=20&format=json"

# API 호출 결과 담기
r = requests.get(url)

# JSON 문자열을 파이썬 객체로 변환
data = r.json()
# print(data)

# 각각의 도서 정보 가져오기
books = []
for d in data['response']['docs']:
  books.append(d['doc'])

# print(books)

# 분석하기 위해 DataFrame 형태로 변환
books_df = pd.DataFrame(books)
print(books_df)