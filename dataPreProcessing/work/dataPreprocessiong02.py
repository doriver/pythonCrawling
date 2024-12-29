# csv파일 특정컬럼 값들 변경후, csv파일로 다시 저장
# csv읽어서 DataFrame으로 받고, DataFrame에서 수정하고, DataFrame을 다시 csv파일

import pandas as pd
import json

csvRead = pd.read_csv(r"D:\pythonCrawling\data\crawlingFile\okky\okkyRookie.csv")

print(csvRead['postReplyLists'].apply(json.dumps))
# csvRead['postReplyLists'] = csvRead['postReplyLists'].apply(json.dumps)
# csvRead.to_csv(r"D:\pythonCrawling\data\crawlingFile\okky\okkyRookie01.csv",encoding ='utf8',index = False)
