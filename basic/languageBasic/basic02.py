## 파이썬 기본 자료형

x = 10
y = 3.14

text = "hello, python"

numbers = [1,2,3,4,5] # list, 순서있는 변경가능한 데이터집합
coordinates = (10, 20) # tuple, 순서있는 변경 불가능한 데이터집합
person = {"name": "alice", "age": 24} # dict, 키와 값의 쌍으로
print(person['name']) # alice
unique_numbers = {1,2,3,3} # set, 중복되지 않는 값들의 집합
print(unique_numbers) # {1, 2, 3}


# len(객체) 객체의 길이(또는 크기)를 반환하는 내장 함수입니다
# 보통 문자열, 리스트, 튜플, 딕셔너리, 세트와 같은 시퀀스 또는 컬렉션 자료형에서 사용
print(len("hello")) # 5
print(len([1,2,3])) # 3
print(len((4,5,6,7))) # 4
print(len({"a":1, "b":2})) # 2
print(len({1,2,3})) # 3


