
# Selenium을 사용하여 크롬으로 Google열기

from selenium import webdriver

# WebDriver 초기화 (Chrome 사용)
driver = webdriver.Chrome()

# 웹사이트 열기
driver.get("https://www.google.com")

# 스크립트 종료 후에 열린브라우저는 닫힘
