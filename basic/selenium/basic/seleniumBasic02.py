
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True) # 브라우저가 스크립트 종료 후에도 닫히지 않도록 유지, 이거 없으면 닫힘

# WebDriver 초기화 (Chrome 사용)
driver = webdriver.Chrome(options=options)

# 웹사이트 열기
driver.get("https://www.google.com")
