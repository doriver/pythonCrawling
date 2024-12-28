from bs4 import BeautifulSoup

tag = "<p class='example' id='test01'> Hello World! </p>" 
soup = BeautifulSoup(tag, 'html.parser') 

# 태그 이름만 특정 
print(soup.find('p'))
 
# 태그 속성만 특정 
print(soup.find(class_='example'))

# 태그 이름과 속성 모두 특정 
print(soup.find('p', class_='example'))

# 셋다 <p class="example" id="test01"> Hello World! </p> 로 출력됨 