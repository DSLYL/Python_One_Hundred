# 由1,2,3,4 能构成多少个不同的三位数
def a():
    count = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and i != k and j != k:
                    print(i, j, k)
                    count += 1
    print("总共组成{0}个三位数".format(count))


a()
