import pandas as pd

csvRead = pd.read_csv(r"D:\pythonCrawling\data\crawlingFile\okky\okkyJobSeeker01.csv")
# 컬럼의 개수 len(df.columns)
print(len(csvRead.columns)) # 10
# 행의 개수 len(df) 
print(len(csvRead)) 
# 특정 컬럼 출력
# print(csvRead['postReplyLists'])