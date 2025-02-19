from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import random
import time
import json
import requests
from bs4 import BeautifulSoup

# 1.7k > 1700변환
def convert_k_to_numbers(num):
    if 'k' in num.lower(): # k있으면 조작해서 반환
        number = float(num.lower().replace('k', ''))
        return int(number * 1000)
    else:
        return int(num) # k없으면 그냥 반환

# 500글자 까지만 허용
def textLengthLimit(text : str) -> str:
    if len(text) > 500:
        return text[0:500] + " ..."
    else:
        return text


driver = webdriver.Chrome()

urlCsv = pd.read_csv(r"D:\pythonCode01\crawling\okky\lifeStory\real\okkyLifeStoryPostUrl500_7.csv")
# urlCsv = pd.read_csv(r"D:\pythonCode01\crawling\okky\lifeStory\real\okkyLifeStoryPostUrl.csv")
linesEs = []

for i in range(len(urlCsv['postUrls'])): # len(urlCsv['postUrls'])
    currentUrl = urlCsv['postUrls'][i]
    driver.get(currentUrl)
    print(f"    =====    =====  count : {i}   ======   ======")
    time.sleep(1 + random.random())

    try:
        ######## 글 뷰 ########
        postView = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]')

        ### 글 작성자 부분
        writerSection = postView.find_element(By.XPATH, './div[1]/div[1]')
        # 작성자
        writer = writerSection.find_element(By.XPATH, './div/*[1]').text
        # 조회수
        _viewCount = writerSection.find_element(By.XPATH, './div/*[last()]/div[last()]').text
        viewCount = convert_k_to_numbers(_viewCount)

        ### 글 부분
        # 글 제목
        title = postView.find_element(By.XPATH, './h1').text
        # 내용, 이미지
        contentBox = postView.find_element(By.XPATH, './div[3]/div/div/div')
        # 글 내용 
        contentEs = contentBox.text
        # 글 이미지
        img = 0
        try:
            img = contentBox.find_element(By.CSS_SELECTOR, 'img').get_attribute("src")
        except:
            pass
        # 좋아요
        likeCount = postView.find_element(By.XPATH, './div[4]/div[2]/div/div[1]/span').text

        # 작성 시간( requests해서 얻어옴 )
        response = requests.get(currentUrl)
        html_text = response.text

        soup = BeautifulSoup(html_text, "html.parser")
        json_data = soup.select_one("#__NEXT_DATA__").get_text()
        json_obj = json.loads(json_data)
        createdAt = json_obj['props']['pageProps']['result']['content']['dateCreated']

        ######## 댓글 뷰 ########
        replyView = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[5]')
        ###### 댓글들
        replyList = replyView.find_elements(By.XPATH, './section/div[3]/ul/li')

        postReplyLists = []
        for reply in replyList:
        ### 댓글
            ### 댓글 작성자 부분
            replyWriterSection = reply.find_elements(By.XPATH, './div')[0]
            # 댓글 작성자 이름, 작성 시간
            replyNameCreate = replyWriterSection.find_elements(By.XPATH, './div')[1]
            # 작성자 이름
            replyWriter = replyNameCreate.find_element(By.XPATH, './*[1]').text # a태그, div태그 상황에 따라 나옴

            ### 댓글 본문 부분
            replyContentSection = reply.find_elements(By.XPATH, './div')[1]
            try:
                _replyText = replyContentSection.find_element(By.CSS_SELECTOR, 'div.tiptap.ProseMirror').text
                replyText = textLengthLimit(_replyText)
            except:
                _replyText = replyContentSection.find_element(By.XPATH, './div').text
                replyText = textLengthLimit(_replyText)

            postReplyLists.append(
                {"replyWriter": replyWriter, "replyText": replyText}
            )

        linesEs.append({
                    "desc": 2, "writer": writer, "title": title, "createdAt": createdAt, 
                    "content": contentEs, "imgSrc": img, "viewCount": viewCount, "likeCount": likeCount,
                    "postReplyLists": json.dumps(postReplyLists) # 
                })
    except:
        continue


# csv파일로 저장
dfEs = pd.DataFrame(linesEs)
dfEs.to_csv(r"D:\pythonCode01\data\crawlingFile\realData\okky\okkyLifeStoryFirstPageUp500Es7.csv",encoding ='utf8',index = False)



