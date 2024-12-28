import requests
from bs4 import BeautifulSoup as bs

# 1. 크롤링할 웹페이지 URL 설정
url = "https://www.dcinside.com/"

# 2. HTTP GET 요청
response = requests.get(url)

# 3. 요청 성공 여부 확인
if response.status_code == 200:
    # 4. HTML 파싱
    soup = bs(response.text, 'html.parser')

    # <div id="top"> 내부의 <a> 태그 선택
    a_tags = soup.select("#top .gnb_bar nav ul.gnb_list a")  # 계층적으로 <a> 태그 선택

    print(a_tags) # 

    # <a> 태그의 텍스트 추출
    links_text = [a.get_text(strip=True) for a in a_tags] 

    # 결과 출력
    print("디시:")
    print("추출된 텍스트:", links_text) 
    # ['갤러리', '게임', '연예/방송', '스포츠', '교육/금융/IT', '여행/음식/생물', '취미/생활', '마이너갤', '미니갤', '인물갤', '갤로그', '디시트렌드', '디시뉴스', 'NFT', '디시게임', '디시위키', '이벤트', '디시콘']
    
else:
    print(f"HTTP 요청 실패: {response.status_code}")