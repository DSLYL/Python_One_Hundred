# “3位水仙花数”是指一个三位整数，其各位数字的3次方和等于该数本身例如
# ：ABC是一个“3位水仙花数”，则：一个的3次方+ B的3次方+ C的3次方= ABC。
# 请按照从小到大的顺序输出所有的3位水仙花数，请用一个“逗号+空格”分隔输出结果。
import random


def a(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += pow(int(i), 3)
    if sum == int(n):
        if sum == 407:
            print('{0}'.format(sum))
        else:
            print('{0}'.format(sum), end=", ")


def main():
    for i in range(1000):
        a(i)


if __name__ == '__main__':
    main()
