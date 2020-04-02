# # 用函数实现如下要求：
# # （1）随机生成20个学生的成绩
# # （2）判断这20个学生成绩的等级
# import random
#
#
# def fun():
#     a = []
#     for i in range(20):
#         # 产生1-100的浮点数
#         i = random.uniform(1, 100)
#         a.append("%.1f" % i)
#     a.sort()
#     a = list(enumerate(a))
#     for i, j in a:
#         if float(j) < 60:
#             print("{0}学生的成绩为{1}, 等级为C".format(i, j))
#         elif float(j) >= 60 and float(j) < 80:
#             print("{0}的成绩为{1}, 等级为B".format(i,j))
#         elif float(j) >= 80 and float(j) <= 100:
#             print("{0}的成绩为{1}, 等级为A".format(i, j))
#
#
# fun()
#
import random
def get_level(score):
    if 90<=score<=100:
        return 'A'
    elif 80<=score<90:
        return 'B'
    elif 70<=score<80:
        return 'C'
    elif 60<=score<70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        print("Error")
        return 'Z'
def main():
    for i in range(20):
        score= random.randint(0,100)
        # print(get_level(score))
        print("The score is %s,the level is %s." %(score,get_level(score)))
main()