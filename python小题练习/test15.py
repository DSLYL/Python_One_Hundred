# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 用三种方法实现

#方法1
# fenzi = 2  # 分子
# fenmu = 1  # 分母
# l = []
# s = 0
#
# for i in range(1, 20 + 1):
#     a = fenzi
#     b = fenmu
#     s += (a / b)
#     l.append('%s/%s' % (a, b))
#     fenzi = a + b
#     fenmu = a
#
# print('+'.join(i for i in l), end='')
# print('=%.2f' % s)

#方法2
# a = 2
# b = 1
# sum = 0
# for i in range(20):
#     sum = a / b + sum
#     a, b = (a + b), a
# print(sum)


#方法3
a1=1
a2=2
s=0
string=''
for i in range(20):
    string+='%d/%d+'%(a2,a1)
    s+=a2/a1
    a1,a2=a2,a1+a2
print(string)
string = string[:-1]
string += "=%.2f" % s
print(string)


