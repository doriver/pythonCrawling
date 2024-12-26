import sys
import os
# 프로젝트 루트 경로를 sys.path에 추가
sys.path.append(os.path.abspath("D:/pythonCode01"))

# 파이썬에서 다른 .py 파일에 정의된 메서드나 사용하려면 import를 활용
import dataPreProcessing.method.dataMethod01 as dm

ex = "1.7k"
print(dm.convert_k_to_numbers(ex)) # 1700