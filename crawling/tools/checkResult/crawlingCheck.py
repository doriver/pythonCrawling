import pandas as pd
import json

csvRead = pd.read_csv(r"D:\pythonCode01\data\crawlingFile\realData\okky\okkyLifeStoryFirstPageUp500Es7.csv")
# csvRead = pd.read_csv(r"D:\pythonCrawling\data\crawlingFile\yes24NewProduct.csv")
# 컬럼의 개수 len(df.columns)
print(len(csvRead.columns)) # 10
# 행의 개수 len(df) 
print(len(csvRead)) 
# 특정 컬럼 출력
# print(csvRead['postReplyLists'])
# print(csvRead['viewCount'])

# csvRead['postReplyLists'] = csvRead['postReplyLists'].apply(json.loads)
# print(csvRead['postReplyLists'][0])

# print(csvRead['postReplyLists'][1])