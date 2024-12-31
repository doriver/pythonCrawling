### 파이썬에서 **슬라이싱(Slicing)**은 시퀀스 자료형(리스트, 문자열, 튜플 등)에서 특정 부분을 추출하는 방법
### sequence[ start : stop : step ]
# start: 슬라이싱을 시작할 인덱스 (포함)  ,/  stop: 슬라이싱을 종료할 인덱스 (포함하지 않음)  ,/  step: 슬라이싱할 간격
# 음수 인덱스: 뒤에서부터 요소를 가리킬 수 있음
# 원본은 변경되지 않음 

str = 'las  dfj,alsjdflaj0001231231321ㅁㄴㅇㄻㄴㅇㄻㄴㅇㄻㄻㄴ'
# print(str[0:2]) # la
# print(str[0:8]) # las  dfj
# print(str[0:9]) # las  dfj,

str01 = 'asd'
print("===")
print(str01[0:500])