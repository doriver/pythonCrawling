import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup

base_url = 'https://www.yes24.com'
main_url = '/Product/Category/NewProduct?categoryNumber=001&pageSize=24&newProductType=NEW'

# 목록뽑아놓고, 각각에 들어가는거임 
lines = []
for page in tqdm(range(1, 3)):
    url = f'{base_url}{main_url}&pageNumber={page}'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    lis = soup.select('#yesNewList > li')
    for index, li in enumerate(lis, start=1 ):
        print(f'{page}페이지 {index}', end='  ')
        try:
            sub_page = li.select_one('.img_grp > a')['href'] # 속성값
            sub_url = f'{base_url}{sub_page}'

            res = requests.get(sub_url)
            book_soup = BeautifulSoup(res.text, 'html.parser')

            imageUrl = book_soup.select_one('#yDetailTopWrap img.gImg')['src']
            title = book_soup.select_one('#yDetailTopWrap div.gd_titArea > h2.gd_name').text.strip()
            author = book_soup.select_one('span.gd_auth > a').text.strip() # 텍스트값
            company = book_soup.select_one('span.gd_pub > a').text.strip()
            price = book_soup.select_one('tr.accentRow em.yes_m').text.strip()
            price = int(price.replace(',','')) # 문자열을 처리하여 정수로 변환
            summary = book_soup.select_one('#infoset_introduce textarea.txtContentText').get_text(separator='\n').strip() 
                                                        # html태그는 제거되고 텍스트만 반환, 여러 텍스트블록이 있을경우 separator인자로 지정된 문자열을 텍스트 사이에 삽입
            lines.append({
                'title': title, 'author': author, 'company': company, 'price': price, 'imageUrl': imageUrl, 'summary': summary
            })
        except:
            continue

df = pd.DataFrame(lines)
len(df)

df.to_csv(r"D:\pythonCrawling\crawlingFile\yes2403.csv",encoding ='utf8',index = False)
# 경로 구분을 의미하는 \가 문자와 만나면 특수문자(이스케이프 시퀀스)로 인식한다. 
# \\로 하거나 경로앞에 r을 붙여준다(raw, 있는 그대로 쓰겠다.)