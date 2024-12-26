
str01 = "asd"
str02 = "qqq"
print(str01 + str02) # asdqqq

# strip()메서드 : 문자열에서 앞뒤 공백이나 특정 문자를 제거하는 데 사용
s = "  Hello World  "
print(s.strip())  # "Hello World"

ss = "--Hel--lo--"
print(ss.strip('-'))  # "Hel--lo"


# 파이썬에서 '' (작은따옴표)와 "" (큰따옴표)는 기능적으로는 차이가 거의 없다, 문자열을 나타냄
string01 = "she said, 'hi'"
string02 = 'she said, "hi"' # 다른 따옴표는 그냥 사용 가능
if string01 != string02: print(string01)  # she said, 'hi'
print(string02) # she said, "hi"
string03 = "he said, \"hello\" girl" # 같은 따옴표는 백슬래시(\)를 사용해야함
print(string03) # he said, "hello" girl
