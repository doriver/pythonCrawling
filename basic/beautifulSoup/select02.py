from bs4 import BeautifulSoup

# HTML 문서 샘플
html = """
<body>
  <div class="gnb_bar"> </div>
  <div id="top" class="dcwrap">
     <div class="gnb_bar"> 가나다라마바사 </div>
  </div>
  <div class="gnb_bar"> </div>
</body>
"""

# BeautifulSoup으로 파싱
soup = BeautifulSoup(html, 'html.parser')

# CSS 선택자로 특정 부모 안의 자식 요소 선택
gnb_bar_in_top = soup.select_one("#top .gnb_bar")  # id가 'top'인 요소 내부의 class 'gnb_bar'

# 결과 출력
if gnb_bar_in_top:
    print("찾은 요소:", gnb_bar_in_top) # <div class="gnb_bar"> 가나다라마바사 </div>
else:
    print("해당 요소를 찾을 수 없습니다.")