#输出乘法口诀表
def main():
    for i in range(1,10):
        for j in range(1,i+1):
            print('{0}*{1}={2}'.format(j,i,i*j),end=" ")
        print()
if __name__ == '__main__':
    main()