# okky - 커뮤니티 - 사는얘기 완성본

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import random
import time

driver = webdriver.Chrome()
lines = [] # 여기에 데이터들 넣을꺼
        
driver.get("https://okky.kr/articles/1523346?topic=life&page=2")
time.sleep(3)

for i in range(20):
    try: # post 크롤링하는거 와야함
        sel01 = driver.find_elements(By.CSS_SELECTOR, "div.w-full.min-w-0.flex-auto > div.min-w-0.flex-auto > div")
        sel02 = sel01[1]
        # sel01: <div> 3개   ,  sel02: <div> 1개 ( 안에 div 6개 들어있음 ) 
        # 저 6개 div를 선택해야해
        sel03 = sel02.find_elements(By.XPATH, './div')
        print(f"6개 나와야함 : {len(sel03)}")

        postSel = sel03[1]
        commentSel = sel03[4]
        postListSel = sel03[5]

        # 글쓴이
        writer = postSel.find_element(By.CSS_SELECTOR, "div.mb-8.flex a.text-gray-900").text.strip()
        # 만들어진 시간, 조회수
        dv01 = postSel.find_element(By.XPATH, './div')
        dv02 = dv01.find_element(By.XPATH, './div')
        dv03 = dv02.find_element(By.XPATH, './div')
        dayAndView = dv03.find_element(By.XPATH, './div')

        daySel = dayAndView.find_elements(By.XPATH, "./span")
        viewSel = dayAndView.find_elements(By.XPATH, "./div")
        day = daySel[2].text.strip()
        view = viewSel[len(viewSel)-1].text.strip()

        # 제목
        title = postSel.find_element(By.CSS_SELECTOR, "h1").text.strip()
        # 글내용
        content = postSel.find_element(By.CSS_SELECTOR, "div.my-6.text-sm.text-gray-700 div.ProseMirror.remirror-editor").text.strip()
        # 글 이미지
        imgUrl=0
        try:
            imgUrl = postSel.find_element(By.CSS_SELECTOR, "div.my-6.text-sm.text-gray-700 div.ProseMirror.remirror-editor > p > div > img").get_attribute("src")
        except:
            pass

        like = postSel.find_elements(By.CSS_SELECTOR, "div.flex.items-center.space-x-1 > div.inline-flex span.-ml-2")
        # 좋아요 수
        likes = like[0].text.strip()


        commentList = commentSel.find_elements(By.CSS_SELECTOR, "div.my-8 > ul.divide-y > li")
        postReplyLists = []
        for comment in commentList:
            try:
                # 댓글 작성자
                commentWriter = comment.find_element(By.CSS_SELECTOR, "div.flex.items-center a.text-gray-900").text.strip()
                # 댓글 작성시간
                com01 = comment.find_elements(By.XPATH, "./div") # 바로 자식만 찾기
                com02 = com01[0].find_elements(By.XPATH, "./div") # 댓글에서 맨위 블록 3부분
                com03 = com02[1].find_elements(By.XPATH, "./div")
                comTime = com03[len(com03)-1].find_element(By.XPATH, "./a").text.strip()
                # 댓글 내용
                commentContent = comment.find_element(By.CSS_SELECTOR, "div.flex div.ProseMirror.remirror-editor.remirror-a11y-dark").text.strip()
                
                postReplyLists.append(
                    {"user": commentWriter, "content": commentContent, "createAt": comTime }
                )
            except:
                continue

        lines.append({
            "category": "okky", "tag": "lifeStory", "user": writer, "title": title,
            "content": content, "imgSrc": imgUrl, "createAt": day, "viewCount": view, "likeCount": likes
            , "postReplyLists": postReplyLists
        })

        postList = postListSel.find_elements(By.CSS_SELECTOR, "div > div > div > ul > li")
        selected = postListSel.find_element(By.CSS_SELECTOR, "div > div > div > ul > li.bg-gray-100")
        nextPostIndex = postList.index(selected) + 1
        print(f"nextPostIndex : {nextPostIndex}")
        nextPostLink = postList[nextPostIndex].find_element(By.CSS_SELECTOR, "div > a.font-normal").get_attribute("href")

        if nextPostIndex > 19: break

        driver.get(nextPostLink) # 다음post로 이동완료
        time.sleep(1 + random.random())

    except:
        continue


# csv파일로 저장
df = pd.DataFrame(lines)
df.to_csv(r"D:\pythonCrawling\crawlingFile\interimReport\okkyData02.csv",encoding ='utf8',index = False)
