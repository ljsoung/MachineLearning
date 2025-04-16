# WebDriver, BeautifulSoup 임포트
from bs4 import BeautifulSoup
from selenium import webdriver

wd = webdriver.Chrome()
wd.get("https://www.coffeebeankorea.com/store/store.asp")       # 매장 찾기 페이지로 이동

wd.execute_script("storePop2(114)")     # 매장 자세히 보기 자바스크립트 함수 호출

html = wd.page_source       # storePop2(114) 함수가 수행된 페이지의 소스코드 저장

soupCB1 = BeautifulSoup(html, 'html.parser')

# print(soupCB1.prettify())

# 매장 이름 리스트 출력하기
store_name_h2 = soupCB1.select("div.store_txt > p.name > span")
# print(store_name_h2)

store_name = store_name_h2[0].next
# print(store_name)

# 매장 주소 리스트 출력하기
store_address_list = soupCB1.select("div.store_txt > p.address > span")
# print(store_address_list)

store_address = store_address_list[2]
# print(store_address)

# 매장 전화번호 리스트 출력하기
store_phone = soupCB1.select("div.store_txt > p.tel > a")
# print(store_phone[2].string)

input()