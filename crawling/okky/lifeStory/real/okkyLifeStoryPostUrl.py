from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import random
import time
import json
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
postUrls=[]

startUrl = "https://okky.kr/articles/1520050?topic=life&page=62"

driver.get(startUrl)
postUrls.append(startUrl)
time.sleep(2 + random.random())

try:
    ######## 글목록, 페이지 뷰 ########
    listPageView = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[6]')

    postListView = listPageView.find_element(By.XPATH, './div/div[1]/ul')
    postList = postListView.find_elements(By.XPATH, './li')

    selected = postListView.find_element(By.CSS_SELECTOR, "ul > li.bg-gray-100")
    nextPostIndex = postList.index(selected) + 1

    for i in range(500):
        print(f"    =====    =====  count : {i}   ======   ======")
        if nextPostIndex > 19:
            print("해당페이지 맨 마지막 글, 다음페이지로 이동 로직 실행")
            ### 페이지 버튼 부분
            pageButtonSection = listPageView.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[6]/div/div[2]/nav')
            pageButtons = pageButtonSection.find_elements(By.XPATH, './button')
            currentButton = pageButtonSection.find_element(By.CSS_SELECTOR, "nav > button.border-blue-500")
            nextPageButtonIndex = pageButtons.index(currentButton) + 1
            nextPageButton = pageButtons[nextPageButtonIndex]
            nextPageButton.click() # 다음페이지로 이동
            time.sleep(1 + random.random())

            ######## 글목록, 페이지 뷰 ########
            listPageView = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[6]')

            postListView = listPageView.find_element(By.XPATH, './div/div[1]/ul')
            postList = postListView.find_elements(By.XPATH, './li')
            try: 
                nextPostLink = postList[0].find_element(By.CSS_SELECTOR, "div > a.font-normal").get_attribute("href")
                nextPostIndex = 1
            except: 
                nextPostLink = postList[1].find_element(By.CSS_SELECTOR, "div > a.font-normal").get_attribute("href")
                nextPostIndex = 2
        else:
            nextPostLink = postList[nextPostIndex].find_element(By.CSS_SELECTOR, "div > a.font-normal").get_attribute("href")
            nextPostIndex = nextPostIndex + 1
        
        postUrls.append(nextPostLink)

except:
    print(" !!! 실패 !!! ")
    

    
line = {'postUrls': postUrls} # 여기에 데이터들 넣을꺼

# csv파일로 저장
df = pd.DataFrame(line)
# df.to_csv(r"D:\pythonCrawling\crawling\okky\lifeStory\real\okkyLifeStoryPostUrl.csv",encoding ='utf8',index = False)
df.to_csv(r"D:\pythonCode01\crawling\okky\lifeStory\real\okkyLifeStoryPostUrl5002.csv",encoding ='utf8',index = False)