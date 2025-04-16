# selenium 패키지 설치 후
from selenium import webdriver


## 1. 크롬 띄우기 ##

# Chrome 브라우저를 띄우기
driver = webdriver.Chrome()

# 구글 이미지 검색 사이트로 이동
URL='https://www.google.co.kr/imghp'
driver.get(url=URL)


## 2. 검색창 원소를 찾아 검색어를 입력하기 ##
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 검색창의 ID 값 = APjFqb
elem = driver.find_element(By.ID, "APjFqb") # By.ID -> ID를 찾겠다
elem.send_keys("봄") # 봄이라는 텍스트를 검색하는 것처럼 행동
elem.send_keys(Keys.RETURN) # Enter키를 치는 것과 동일


## 3. 페이지 다운키를 누르면서 계속 사진 보기 ##
import time

time.sleep(3)           # 페이지가 로딩될 때까지 기다리기

elem = driver.find_element(By.TAG_NAME, "body") # By.TAG_NAME을 기준으로 함

for i in range(10): # 원하는 횟수만큼 파라미터에 값을 넣으면 됨
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)


## 4. 이미지 링크 주소를 저장하기 ##
links=[]

# 여러 개를 가져오기 위해 elements로 작성
images = driver.find_elements(By.CSS_SELECTOR, "#rso > div > div > div.wH6SXe.u32vCb > div > div > div > div:nth-child(2) > h3 > a > div > div > div > g-img > img")

for image in images:

    img_src = image.get_attribute('src')

    if (img_src is not None) and ('http' in img_src):
        links.append(image.get_attribute('src'))
        print(image.get_attribute('src'))

print(' 찾은 이미지 개수: ', len(links))


## 5. 크롤링한 이미지 다운로드 받기
import urllib.request
import os

os.mkdir('images')

for i, k in enumerate(links):
    url = k
    urllib.request.urlretrieve(url, './images/' + str(i) + ".jpg")

print('다운로드를 완료하였습니다.')

input()

