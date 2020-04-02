# # 题目：求1+2!+3!+...+20!的和
# # 用两种方法实现
def a():
    sum = 0
    for i in range(1,21):
        s1 = 1
        j = 1
        while j<=i:
            s1=s1*j
            j+=1
        sum += s1
    print(sum)
if __name__ == '__main__':
    a()
sum = 0
x = 1
for i in range(1,21):
    x = x * i
    sum = sum + x
print(sum)