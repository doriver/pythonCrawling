import pandas as pd

# 데이터프레임 생성
# data = {'Name': ['Alice', 'Bob'], 'Comment': ['asdf,qwe,nnn', 'hello,world']}
data = [
    {"name": "alice", "comment": "asf,qwe,mnn", "region": "se,oul", "str": "hhhh" ,"age": 12},
    {"name": "bob", "comment": "hello,world", "region": "bu,san", "str": "fff", "age": 99}
]
df = pd.DataFrame(data)

# CSV 저장
df.to_csv('commaTestQouting01.csv', encoding ='utf8', index=False, quoting=1)
df.to_csv('commaTestNoOption01.csv', encoding ='utf8', index=False)