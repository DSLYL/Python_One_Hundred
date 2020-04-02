# # 题目：打印出杨辉三角形
# def a():
#     N = [1]
#     for i in range(10):  # 打印10行
#         print(N)
#         N.append(0)
#         N = [N[k] + N[k - 1] for k in range(i + 2)]
# a()

a = []
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)
for i in range(10):
    a[i][0] = 1
    a[i][i] = i
for i in range(2, 10):
    for j in range(1, i):
        a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

from sys import stdout

for i in range(10):
    for j in range(i + 1):
        stdout.write(str(a[i][j]))
        stdout.write(" ")
    print()