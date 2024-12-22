import requests
# 파이썬에서 HTTP 요청을 간단하게 처리할 수 있는 라이브러리
# 다양한 HTTP 메서드 지원, 요청 시 헤더, 파라미터, 쿠키 설정, ...

response01 = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response01.status_code)  # HTTP 상태 코드
print(response01.text)         # 응답 내용

data = {"title": "foo", "body": "bar", "userId": 1}
response02 = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response02.status_code)  # 상태 코드
print(response02.json())       # JSON 응답