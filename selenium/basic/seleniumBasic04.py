
# Selenium을 사용하여 Google에서 검색 + 검색결과 크롤링

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

options = Options()
options.add_experimental_option("detach", True) # 브라우저가 스크립트 종료 후에도 닫히지 않도록 유지, 이거 없으면 닫힘

# WebDriver 초기화 (Chrome 사용)
driver = webdriver.Chrome(options=options)

# 웹사이트 열기
driver.get("https://www.google.com")

# 검색창 찾기
search_box = driver.find_element(By.NAME, "q")

# 검색어 입력 및 검색
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN) # 엔터 키 입력

time.sleep(3)

# 검색 결과 출력
results = driver.find_elements(By.CSS_SELECTOR, "h3")
for result in results:
    print(result.text)