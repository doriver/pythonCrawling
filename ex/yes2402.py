import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup

base_url = 'https://www.yes24.com'
main_url = '/Product/Category/NewProduct?categoryNumber=001&pageSize=24&newProductType=NEW'
url = f'{base_url}{main_url}&pageNumber=1'
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
# result = requests.get(url, headers=header)
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
lis = soup.select('#yesNewList > li')
len(lis)

# 목록뽑아놓고, 각각에 들어가는거임 
lines = []
for index, li in enumerate(lis):
    print(index, end='  ')
    try:
        sub_page = li.select_one('.img_grp > a')['href']
        sub_url = f'{base_url}{sub_page}'

        res = requests.get(sub_url)
        book_soup = BeautifulSoup(res.text, 'html.parser')

        imageUrl = book_soup.select_one('#yDetailTopWrap img.gImg')['src']
        title = book_soup.select_one('#yDetailTopWrap div.gd_titArea > h2.gd_name').text.strip()
        author = book_soup.select_one('span.gd_auth > a').text.strip()
        company = book_soup.select_one('span.gd_pub > a').text.strip()
        price = book_soup.select_one('tr.accentRow em.yes_m').text.strip()
        price = int(price.replace(',',''))
        summary = book_soup.select_one('#infoset_introduce textarea.txtContentText').get_text(separator='\n').strip()

        lines.append({
            'title': title, 'author': author, 'company': company, 'price': price, 'imageUrl': imageUrl, 'summary': summary
        })
    except:
        continue

df = pd.DataFrame(lines)
len(df)

df.to_csv(r"D:\pythonCrawling\crawlingFile\yes24.csv",encoding ='utf8',index = False)
# 경로 구분을 의미하는 \가 문자와 만나면 특수문자(이스케이프 시퀀스)로 인식한다. 
# \\로 하거나 경로앞에 r을 붙여준다(raw, 있는 그대로 쓰겠다.)