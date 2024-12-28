### 파이썬에서 **슬라이싱(Slicing)**은 시퀀스 자료형(리스트, 문자열, 튜플 등)에서 특정 부분을 추출하는 방법
### sequence[ start : stop : step ]
# start: 슬라이싱을 시작할 인덱스 (포함)  ,/  stop: 슬라이싱을 종료할 인덱스 (포함하지 않음)  ,/  step: 슬라이싱할 간격
# 음수 인덱스: 뒤에서부터 요소를 가리킬 수 있음
# 원본은 변경되지 않음 

       # 012345  : '1,234원'의 인덱스 , 길이는 6임
price = '1,234원'
print(price[:-1]) # 1,234   문자열의 처음부터 마지막 문자 바로 앞까지를 선택, 마지막 문자를 제외한 모든 부분을 가져옴
print(price[-1]) # 원       마지막 문자
print(price[1:]) # ,234원   첫 번째 문자부터 끝까지

print(price[1:4:1]) # ,23
print(price[1:4:2]) # ,3
print(price[2:5]) # 234
print(price[2:6]) # 234원

            # 0   1    2    3    4   ,  길이는 5  
hundList = [100, 200, 300, 400, 500]
print(hundList[0:3:2]) # [100, 300]

print(hundList[2:]) # [300, 400, 500]
print(hundList[:3]) # [100, 200, 300]
print(hundList[1:3]) # [200, 300]
print(hundList[::2]) # [100, 300, 500]
print(hundList[::-1]) # [500, 400, 300, 200, 100]
print(hundList[::-2]) # [500, 300, 100]

