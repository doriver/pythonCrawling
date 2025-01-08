
# csvRead = pd.read_csv(r"D:\pythonCode01\data\crawlingFile\realData\okky\okkyLifeStoryLastPage.csv")

# DataFrame에서 row추출


# for i in range(len(newDf['postReplyLists'])):
#     print(newDf['postReplyLists'].iloc[i])


# aa01 = newDf['content'].apply(str.replace('\r\n', '<br>'))
# print("   =======    ======      =======    ======      =======    ======  ")
# print("   =======    ======      =======    ======      =======    ======  ")




# print(len(newDf['postReplyLists'])) # 3

# data =[]
# series = newDf['postReplyLists']
# for i in range(len(series)):
#     bb = series.iloc[i] # newDf['postReplyLists'].iloc[i]
#     data = json.loads(bb)

#     for j in range(len(data)):
#         data[j]['replyText'] = data[j]['replyText'].replace('\n', '<br>')

#     series.iloc[i] = json.dumps(data)

# newDf['postReplyLists'] = series





# bb01 = newDf['postReplyLists'].iloc[0]
# # print(bb01)
# # print( type(bb01) ) # <class 'str'>
# data = json.loads(bb01) # json문자열을 python객체로 변환
# # print( type(data)) # <class 'list'>
# # print( type(data[0])) # <class 'dict'>

# print(data)

# print(data[0]['replyText'].replace('\n', '<br>')) # br변경되서 나오고
# data[0]['replyText'] = data[0]['replyText'].replace('\n', '<br>')



# csvRead['createAt'] = csvRead['createAt'].apply(dm.timeConvert)