# csv파일 특정컬럼 값들 변경후, csv파일로 다시 저장
# csv읽어서 DataFrame으로 받고, DataFrame에서 수정하고, DataFrame을 다시 csv파일

import pandas as pd

csvRead = pd.read_csv(r"D:\pythonCrawling\data\crawlingFile\okky\okkyJobSeeker01.csv")

import sys
import os
# 프로젝트 루트 경로를 sys.path에 추가
sys.path.append(os.path.abspath("D:\pythonCrawling"))

# 파이썬에서 다른 .py 파일에 정의된 메서드나 사용하려면 import를 활용
import dataPreProcessing.method.dataMethod01 as dm

csvRead['createAt'] = csvRead['createAt'].apply(dm.timeConvert)
csvRead['viewCount'] = csvRead['viewCount'].apply(dm.convert_k_to_numbers)
csvRead.to_csv(r"D:\pythonCrawling\data\crawlingFile\okky\okkyRookie.csv",encoding ='utf8',index = False)
