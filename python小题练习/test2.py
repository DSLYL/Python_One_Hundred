
#求完全数
def fun(n):
    global a
    b = []
    for i in range(1, n):
        if n % i == 0:
            b.append(i)
            a = sum(b)
    if a == n:
        return 1
    else:
        return 0


if __name__ == '__main__':
    # r = fun(int(eval(input("输入要判断的数字："))))
    # print(r)
    i = 2
    while i < 1001:
        r1 = fun(i)
        if r1 == 1:
            print(i)
        i += 1
