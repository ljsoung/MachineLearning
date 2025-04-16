# WebDriver 임포트
from selenium import webdriver

wd = webdriver.Chrome()             # 크롬 WebDriver 객체 생성
wd.get("https://www.google.com")    # 크롬으로 웹페이지 열기

input("브라우저를 닫으려면 엔터를 누르세요.")