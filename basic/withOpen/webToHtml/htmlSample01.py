import requests 

# 가져올 url 문자열로 입력
url = 'https://okky.kr/articles/1523810?topic=life&page=1'
response = requests.get(url)
html_text = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_text, "html.parser")
formatted_html =  soup.prettify()

file_path = r'D:\pythonCrawling\data\html\aatest.html'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(formatted_html)

print(f"HTML이 '{file_path}'에 저장되었습니다.")