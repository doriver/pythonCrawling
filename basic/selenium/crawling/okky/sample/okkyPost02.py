# html쪽에서 막혔다가 , 선택한 selenium객체를 html으로하고, 보기좋게해서, html파일로 만들어버림 

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
lines = [] # 여기에 데이터들 넣을꺼

driver.get("https://okky.kr/articles/1523255?topic=community&page=1")
time.sleep(4)

sel01 = driver.find_elements(By.CSS_SELECTOR, "div.w-full.min-w-0.flex-auto > div.min-w-0.flex-auto > div")
sel02 = sel01[1]
# sel01: <div> 3개   ,  sel02: <div> 1개 ( 안에 div 6개 들어있음 ) 
# 저 6개 div를 선택해야해
sel03 = sel02.find_elements(By.XPATH, './div')
print(len(sel03))

postSel = sel03[1]
commentSel = sel03[4]
postListSel = sel03[5]

title = postSel.find_element(By.CSS_SELECTOR, "h1").text
writer = postSel.find_element(By.CSS_SELECTOR, "div.mb-8.flex a.text-gray-900").text
writerLink = postSel.find_element(By.CSS_SELECTOR, "div.mb-8.flex a.text-gray-900").get_attribute("href")
content = postSel.find_element(By.CSS_SELECTOR, "div.my-6.text-sm.text-gray-700 div.ProseMirror.remirror-editor").text

like = postSel.find_elements(By.CSS_SELECTOR, "div.flex.items-center.space-x-1 > div.inline-flex span.-ml-2")
likes = like[0].text
disLikes = like[1].text

commentList = commentSel.find_elements(By.CSS_SELECTOR, "div.my-8 > ul.divide-y > li")
comment = commentList[0]
commentWriter = comment.find_element(By.CSS_SELECTOR, "div.flex.items-center a.text-gray-900").text
commentWriterUrl = comment.find_element(By.CSS_SELECTOR, "div.flex.items-center a.text-gray-900").get_attribute("href")
commentContent = comment.find_element(By.CSS_SELECTOR, "div.flex div.ProseMirror.remirror-editor.remirror-a11y-dark").text

lines.append({
    "title": title, "writer": writer, "content": content, "likes": likes, "disLikes": disLikes
    , "commentWriter": commentWriter, "commentContent": commentContent
})
print(lines)