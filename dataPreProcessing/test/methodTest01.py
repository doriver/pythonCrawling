# 파이썬에서 다른 .py 파일에 정의된 메서드나 사용하려면 import를 활용
import dataPreProcessing.method.dataMethod01 as dm

# 상대 경로 import
# from ..method.dataMethod01 import 함수이름


ex = "1.7k"
print(dm.convert_k_to_numbers(ex)) # 