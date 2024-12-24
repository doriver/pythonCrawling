from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()

lines = [] # 여기에 데이터들 넣을꺼



for i in range(10): # 페이지당 글 20개
    try:
        driver.get("https://okky.kr/community?page=1")
        time.sleep(4)

        results = driver.find_element(By.CSS_SELECTOR, "div.overflow-hidden > ul.divide-y")
        list = results.find_elements(By.XPATH, "//li[contains(@class, 'py-3.5')]")

        li = list[i]
        section = li.find_elements(By.CSS_SELECTOR, "div.flex.flex-col > div")

        # 글쓴이
        writer = section[0].find_element(By.CSS_SELECTOR, "a.truncate").text.strip()
        print(writer)
        # 글 제목부분
        target = section[1].find_element(By.CSS_SELECTOR, "a")
        title = target.text.strip()

        # 조회수, 좋아요, 댓글수
        numbers = section[2].find_elements(By.CSS_SELECTOR, "div.text-gray-700 > div")
        # 조회수
        views = numbers[0].find_element(By.CSS_SELECTOR, "span").text.strip()
        # 좋아요수
        likes = numbers[1].find_element(By.CSS_SELECTOR, "span").text.strip()
        # 댓글 수
        comments = numbers[2].find_element(By.CSS_SELECTOR, "span").text.strip()

        # detail로 이동
        driver.get(target.get_attribute("href"))
        time.sleep(2)
        # 본문내용
        content = driver.find_element(By.CSS_SELECTOR, "div.mb-14.mt-8.w-full > div.my-6.text-sm.text-gray-700 div.ProseMirror.remirror-editor").text.strip()
        
        lines.append({
            'writer': writer, 'title': title, 'views': views, 'likes': likes, 'comments':comments,'content': content
        })
    except:
        continue

df = pd.DataFrame(lines)

df.to_csv(r"D:\pythonCode01\crawlingFile\okkySample01.csv",encoding ='utf8',index = False)
