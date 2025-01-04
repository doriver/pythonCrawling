
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import random
import time
import json

# 가져올 url 문자열로 입력
url = "https://okky.kr/articles/1523810?topic=life&page=1"

driver = webdriver.Chrome()
driver.get(url)

page_source = driver.page_source

from bs4 import BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")
formatted_html =  soup.prettify()
              
file_path = r'D:\pythonCrawling\data\html\sstest.html'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(formatted_html)

print(f"HTML이 '{file_path}'에 저장되었습니다.")