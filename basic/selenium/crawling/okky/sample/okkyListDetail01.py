from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://okky.kr/community?page=1")
time.sleep(3)

results = driver.find_element(By.CSS_SELECTOR, "div.overflow-hidden > ul.divide-y")
list = results.find_elements(By.XPATH, "//li[contains(@class, 'py-3.5')]")

li = list[2] # 글목록 20개중 하나 지정한거
section = li.find_elements(By.CSS_SELECTOR, "div.flex.flex-col > div")

# 글쓴이
writer = section[0].find_element(By.CSS_SELECTOR, "a.truncate")
print(writer.text)

# 글 제목부분
target = section[1].find_element(By.CSS_SELECTOR, "a")
print(target.text)
print(target.get_attribute("href"))

# 조회수, 좋아요, 댓글수
numbers = section[2].find_elements(By.CSS_SELECTOR, "div.text-gray-700 > div")
# 조회수
views = numbers[0].find_element(By.CSS_SELECTOR, "span")
print(views.text)
# 좋아요수
likes = numbers[1].find_element(By.CSS_SELECTOR, "span")
print(likes.text)
# 댓글 수
comments = numbers[2].find_element(By.CSS_SELECTOR, "span")
print(comments.text)

# detail로 이동
driver.get(target.get_attribute("href"))
time.sleep(3)
# 본문내용
detail = driver.find_element(By.CSS_SELECTOR, "div.mb-14.mt-8.w-full > div.my-6.text-sm.text-gray-700 div.ProseMirror.remirror-editor")
print(detail.text)