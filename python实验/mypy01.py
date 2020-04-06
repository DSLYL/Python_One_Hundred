# a= 3.55553
# print("%7.3f"%a)
#
# import numpy as np
# x = np.ones(3)
# m = np.eye(3)*3
# m[0,2] = 5
# m[2,0] = 3
# print("矩阵{0}和\n矩阵{1}\n相乘的结果是{2}：".format(x, m, x@m))
#
# x=['aaa', 'bc', 'd', 'b', 'ba']
# print(sorted(x, key=lambda item:(len(item),item)))
#

# 所提交的代码
# 输入一位三位数，输出它的百位，十位，个位

x= (input())
a, b, c = map(int, x)
print(a, b, c)

#输入三个英文字母，按顺序输出

s = input('x, y, z=')
x, y, z = s.split(',')
x, y, z = sorted([x, y, z])
print(x, y, z)