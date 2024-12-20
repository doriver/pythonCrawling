if 4 in [1,2,3,4]: print("if문 작동 4가 있따")

languages = ['python', 'perl', 'c', 'java']

for lang in languages :
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")