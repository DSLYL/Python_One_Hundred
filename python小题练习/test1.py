#求和  1~100 3种方法
def t():
    a = []
    for i in range(1, 101):
        a.append(i)
    sum1 = sum(a)
    print(sum1)


t()


def t1():
    sum = 0
    for i in range(1, 101):
        sum = sum + i
    print(sum)


t1()


from functools import reduce


def t2():
    tt = reduce(lambda x, y: x + y, [x for x in range(1, 101)])
    print(tt)


t2()
