from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://dhlottery.co.kr/common.do?method=main')

num_view = driver.find_element(By.ID, 'numView')
num_comp = num_view.find_elements(By.XPATH, "*")

numbers = [c.text for c in num_comp[1:7]] 
bonus = num_comp[-1].text # 보너스 숫자도 빼먹으면 안됨

print(numbers)
print(bonus)