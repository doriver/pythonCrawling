lines = []

postReplyLists = []

postReplyLists.append({    "wirter": "홍길동", "viewCount": 3 })
postReplyLists.append({    "wirter": "이순신", "viewCount": 7 })


lines.append({
    "title": "춥네", "likeCount": 5, "postReplyLists": postReplyLists
})


file_path = r'D:\pythonCrawling\data\py\data02.py'
# .py 파일로 저장
with open(file_path, "w", encoding='utf-8') as file:
    file.write(f"data = {lines}")