from pypinyin import pinyin
while True:
    try:
        line = input()
    except EOFError as e:
        break
    line = line.replace(" ","")
    py = pinyin(line)
    py = map(lambda x:x[0], py )
    print(" ".join(list(" ".join(py).replace(" ","|" ))))

