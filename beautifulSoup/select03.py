from bs4 import BeautifulSoup

# HTML 문서 샘플
html = """
<body>
  <div id="top" class="dcwrap">
     <div class="gnb_bar"> 
         <nav class="gnb clear">
             <ul class="gnb_list clear">
                <li>  <a href=""> 갤러리 </a>  </li>
                <li>  <a href=""> 마이너갤 </a>  </li>
                <li>  <a href=""> 미니갤</a>  </li>
             </ul>
         </nav>
      </div>
  </div>
</body>
"""

# BeautifulSoup으로 파싱
soup = BeautifulSoup(html, 'html.parser')

# <div id="top"> 내부의 <a> 태그 선택
a_tags = soup.select("#top .gnb_bar nav ul.gnb_list a")  # 계층적으로 <a> 태그 선택

print(a_tags) # [<a href=""> 갤러리 </a>, <a href=""> 마이너갤 </a>, <a href=""> 미니갤</a>]

# <a> 태그의 텍스트 추출
links_text = [a.get_text(strip=True) for a in a_tags] 

# 결과 출력
print("추출된 텍스트:", links_text) # ['갤러리', '마이너갤', '미니갤']