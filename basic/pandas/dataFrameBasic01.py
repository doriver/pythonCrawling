import pandas as pd

data = {
    'Name' : ['Alice','Bob','Charlie'],
    'Age' : [25, 30, 35],
    'City' : ['New york', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
# print(df) # 재밌게 출력됨
print(df.info()) # Column(열)마다 Dtype 등이 출력됨
# print(df['Name']) # Name컬럼 출력됨

df02 = pd.DataFrame([
    {'Name': 'Alice' , 'Age': 25 , 'City': 'New york'}
    , {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'}
    , {'Name': 'Charlie' , 'Age': 35, 'City': 'Chicago'}
])
print(df02)
# iloc : 위치기반 인덱스
print(df02.iloc[0, 1]) # 첫번째 행, 두번째 열 = 25
# # loc : 컬럼기반 인덱싱
# print(df02.loc[1 , 'City']) # 두번째행, 'City'열 = Los Angeles
# 특정 열 선택
print(df02['City'])

df03 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})
df03['B'] = df03['B'].apply(lambda x: x*2 if x > 5 else x)
print(df03) # B열 마지막값이였던 6만 12로 변함