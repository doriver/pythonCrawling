# 1.7k > 1700변환
def convert_k_to_numbers(num):
    if 'k' in num.lower(): # k있으면 조작해서 반환
        number = float(num.lower().replace('k', ''))
        return int(number * 1000)
    else:
        return int(num) # k없으면 그냥 반환

# 500글자 까지만 허용
def textLengthLimit(text : str) -> str:
    if len(text) > 500:
        return text[0:500] + " ..."
    else:
        return text
    



# def timeConvert(str : str):
#     if "일 전" in str:
#         return str.replace("일 전", "")
#     elif "일전" in str:
#         return str.replace("일전", "")
#     elif "시간 전" in str:
#         str1 = str.replace("시간 전", "")
#         return str1.replace("약 ", "")
    