import pandas as pd

data = {
    'Name' : ['Alice','Bob','Charlie'],
    'Age' : [25, 30, 35],
    'City' : ['New york', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df) # 재밌게 출력됨
print(df.info()) # Column(열)마다 Dtype 등이 출력됨
print(df['Name']) # Name컬럼 출력됨


# df.to_csv(r"D:\pythonCrawling\crawlingFile\interimReport\okkyData02.csv",encoding ='utf8',index = False)
csvRead = pd.read_csv(r"D:\pythonCode01\crawlingFile\okkyThree.csv")
print(csvRead) # [3 rows x 10 columns] 대략적으로만 출력됨
