from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://dhlottery.co.kr/common.do?method=main')

num_view = driver.find_element(By.ID, 'numView')
num_comp = num_view.find_elements(By.XPATH, "*") # 이거로 js 뽑는건가? > 아닌듯

numbers = [c.text for c in num_comp[1:7]] 
bonus = num_comp[-1].text # 보너스 숫자도 빼먹으면 안됨

print(numbers)
print(bonus)



#### num_view = driver.find_element(By.ID, 'numView') 결과물 
# <selenium.webdriver.remote.webelement.WebElement 
# (session="389b18b1dfbd10b3166b953a65076cd3"
# , element="f.A42F4E2555CF2758C585963E6FC5B863.d.E695279D5F0206D6DB4050265252582B.e.120")>

#### num_comp = num_view.find_elements(By.XPATH, "*") 결과물
# [ ] 안에 위와 똑같은 형태로 여러개 들어있음
# <selenium.webdriver.remote.webelement.WebElement (session="389b18b1dfbd10b3166b953a65076cd3", element="f.A42F4E2555CF2758C585963E6FC5B863.d.E695279D5F0206D6DB4050265252582B.e.175")>]
