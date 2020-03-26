with open(r"aa.txt", "r", encoding="utf-8") as f:
    # print(f.read(4))
    # print(f.read())
    # print(f.readlines())
    # print(f.readline())
    while True:
        fra=f.readline()
        if not fra:
            break
        else:
            print(fra,end="")
