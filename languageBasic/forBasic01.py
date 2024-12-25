for i in range(10): # 0 ~ 3까지만 진행됨
    try:
        print(i)
        if i == 3: break
    except:
        continue