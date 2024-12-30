import pandas as pd

df = pd.DataFrame({})
# 따옴표로 감싸도록 설정 하는거 일껄
df.to_csv('file.csv', index=False, quoting=1)  # quoting=1은 csv.QUOTE_MINIMAL에 해당
# pandas가 값을 따옴표로 감싸 데이터 무결성을 보장

# 데이터 값에 줄바꿈 문자(\n 또는 \r\n)가 포함된 경우, pandas는 기본적으로 줄바꿈을 따옴표로 감싸 처리

# NaN 값이 CSV로 저장될 때 기본적으로 NaN 문자열로 저장됨
# 이를 다른 값으로 바꾸고 싶다면 na_rep 옵션을 사용
df.to_csv('file.csv', index=False, na_rep='NULL')  # NaN을 'NULL'로 대체