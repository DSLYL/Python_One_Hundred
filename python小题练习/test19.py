# 题目：打印出杨辉三角形
def a():
    N = [1]
    for i in range(10):  # 打印10行
        print(N)
        N.append(0)
        N = [N[k] + N[k - 1] for k in range(i + 2)]
a()
