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



html02 = """
<div id="infoset">
    <p>Title: Python Programming</p>
    <p>Author: John Doe</p>
</div>
"""
soup02 = BeautifulSoup(html02, 'html.parser')
text01 = soup02.select_one('#infoset').get_text()
# html태그는 제거되고 텍스트만 반환, 여러 텍스트블록이 있을경우 separator인자로 지정된 문자열을 텍스트 사이에 삽입
text02 = soup02.select_one('#infoset').get_text(separator='\n')
print(text01)
print(text02)
