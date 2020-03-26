def a(a1):
    a1=str(a1)
    sum=0
    for i in a1:
        sum += pow(int(i), 2)
    if sum == 1 or sum == 145:
        return a1


if __name__ == '__main__':
    # a1 = str(eval(input("输入数字")))
    for i in range(10000):
        flag=a(i)
        if flag:
            print("第{0}个数的平方和为".format(i))
