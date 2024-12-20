from bs4 import BeautifulSoup

# HTML 문서 샘플
html = """
<body>
  <div id="top" class="dcwrap">
     <div class="gnb_bar"> 가나다라마바사 </div>
   </div>
</body>
"""

# BeautifulSoup으로 파싱
soup = BeautifulSoup(html, 'html.parser')

# CSS 선택자로 <div class="gnb_bar"> 요소 선택
gnb_bar_div = soup.select_one("div.gnb_bar")  # 클래스가 gnb_bar인 div 중 첫 번째를 선택

# 결과 출력
if gnb_bar_div:
    print("찾은 요소:", gnb_bar_div) # <div class="gnb_bar"> 가나다라마바사 </div>
else:
    print("해당 요소를 찾을 수 없습니다.")