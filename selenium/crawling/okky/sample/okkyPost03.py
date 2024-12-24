# post아래쪽에있는 list에서 현재글 다음글 클릭하는거 해야함

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
lines = [] # 여기에 데이터들 넣을꺼

driver.get("https://okky.kr/articles/1523324?topic=community&page=1")
time.sleep(4)

sel01 = driver.find_elements(By.CSS_SELECTOR, "div.w-full.min-w-0.flex-auto > div.min-w-0.flex-auto > div")
sel02 = sel01[1]
# sel01: <div> 3개   ,  sel02: <div> 1개 ( 안에 div 6개 들어있음 ) 

from bs4 import BeautifulSoup

raw_html = sel02.get_attribute('outerHTML')
soup = BeautifulSoup(raw_html, "html.parser")
formatted_html =  soup.prettify()

file_path = r'D:\pythonCode01\html\output.html'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(formatted_html)

print(f"HTML이 '{file_path}'에 저장되었습니다.")
