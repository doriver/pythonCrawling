for i in range(3): # 0, 1, 2
    print(i)


for i in range(2, 5): # 2, 3, 4
    print(i)

# for문 range(start, stop, step) 끝값은 포함x

for i in range(5):
    if i == 2:
        continue # 현재 반복을 건너뛰고 다음 반복으로 넘어감
    print(i) # 0 1 3 4


for i in range(10): # 0 ~ 3까지만 진행됨
    print(i)
    if i == 3: break # 반복문을 빠져나옴
   