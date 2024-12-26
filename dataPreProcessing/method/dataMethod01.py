# 1.7k > 1700변환
def convert_k_to_numbers(num):
    if 'k' in num.lower(): # k있으면 조작해서 반환
        number = float(num.lower().replace('k', ''))
        return int(number * 1000)
    else:
        return int(num) # k없으면 그냥 반환

