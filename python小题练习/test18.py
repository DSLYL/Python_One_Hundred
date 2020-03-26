# 请编写一个函数fun()，它的功能是：生成n（n为奇数）阶幻方，即每行、每列、对角线之和均相等。
# def fun(a,n):

from math import sqrt
def fun(a):
    num=0
    for i in range(0,int(sqrt(a))+1):
        for j in range(0,i+1):
            for k in range(0,j+1):
                for l in range(0,k+1):
                    if (i**2+j**2+k**2+l**2==a):
                        num+=1
                        print(('{}*{}+{}*{}+{}*{}+{}*{}={}').format())