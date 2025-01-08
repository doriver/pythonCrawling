import pandas as pd
import json

csvRead = pd.read_csv(r"D:\pythonCode01\data\crawlingFile\realData\okky\okkyLifeStoryFirstPageUp500Es7.csv")

aa01 = csvRead['content'].str.replace('\r\n', '<br>')
aa02 = aa01.str.replace('\n', '<br>')
aa03 = aa02.str.replace('\r', '<br>')
# print(type(aa03)) # <class 'pandas.core.series.Series'>
csvRead['content'] = aa03


csvRead.to_csv(r"D:\pythonCode01\data\crawlingFile\processedData\okkyLifeStory500Es07.csv",encoding ='utf8',index = False)


