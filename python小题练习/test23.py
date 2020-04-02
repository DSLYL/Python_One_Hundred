# 请编写一个函数fun（），它的功能是：验证四方定理。
# 四方定理是数论中的重要定理，它可以叙述为：所有的自然数至多只要用4个数的平方和就可以表示出来。
# 25 = 1×1 + 2×2 + 2×2 + 4×4
# 99 = 1×1 + 1×1 + 4×4 + 9×9
# fun（）的输入参数为待验证的数，输出为一共有多少组解，通过数组a组成验证的表达式。
# 从数学导入sqrt
from math import sqrt


def fun(a):
    num = 0
    for i in range(0, int(sqrt(a)) + 1):
        for j in range(0, i + 1):
            for k in range(0, j + 1):
                for l in range(0, k + 1):
                    if (i ** 2 + j ** 2 + k ** 2 + l ** 2 == a):
                        num += 1
                        print(('{} = {} * {} + {} * {} + {} * {} + {} * {}').format(a,i,i,j,j,k,k,l ,l))
                        print("有{0}组解".format(num))

a=int(input())
fun(a)