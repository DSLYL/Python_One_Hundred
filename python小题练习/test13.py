# 用*号输出字母C的图案。
# spaceNum = [30, 25, 18, 15, 12, 10, 8, 6, 5, 4, 3, 3]
spaceNum=[20,18,16,14,12,10,8,6,4,3,3,3,]
space = ' '
star = '*'
for i in range(1, len(spaceNum)):
    print(spaceNum[i] * space, star)

spaceNum.reverse()
for i in range(1, len(spaceNum)):
    print(spaceNum[i] * space, star)