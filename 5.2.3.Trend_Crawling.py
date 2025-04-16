# selenium 패키지 설치 후
from selenium import webdriver
from selenium.webdriver.common.by import By


## 1. 크롬 띄우기 ##

# Chrome 브라우저를 띄우기
driver = webdriver.Chrome()


## 2. 네이버 실시간 검색어 크롤링 ##
URL='https://signal.bz/news'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)

naver_results = driver.find_elements(By.CSS_SELECTOR, "#app > div > main > div > section > div > section > section:nth-child(2) > div > div > div > div > div > span.rank-text")

naver_list = []
for naver_result in naver_results:
    naver_list.append(naver_result.text)


## 3. 줌 실시간 검색어 크롤링 ##
import time

URL='https://zum.com'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)

driver.find_element(By.CSS_SELECTOR, '#search-input').send_keys("아무거나 검색")
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, '#app > div.wrap > header > div.search_bar > div > fieldset > div > button.search > img').click()
time.sleep(1)

zum_results = driver.find_elements(By.CSS_SELECTOR, '#issue_wrap > ul > li > div > a:nth-child(1) > span.txt')

zum_list = []
for zum_result in zum_results:
    zum_list.append(zum_result.text)


## 4. 실시간 검색어 출력하기
print("네이버", naver_list)
print("줌", zum_list)