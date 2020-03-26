# ：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
def a(a1):
    a2 = list()
    a4 = 0
    while a4 != 1:
        for i in range(2, a1 + 1):
            a4, k = divmod(a1, i)
            if k == 0:
                a2.append(i)
                a1 = a4
                break
            else:
                continue
    return a2


def main():
    aa = int(input())
    b = a(aa)
    print('{0}='.format(aa), end="")
    for i in range(len(b)):
        if i==len(b)-1:
            print("{0}".format(b[i]))
        else:
            print("{0}*".format(b[i]), end="")


if __name__ == '__main__':
    main()
