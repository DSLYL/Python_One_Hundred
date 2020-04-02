# try:
#     f = open(r'a.txt','r')
#     content = f.readline()
#     print(content)
# except:
#     print('文件没有找到')
# finally:
#     print('关闭文件')
#     # 有可能文件不存在，使得f创建失败
#     # f.close()
#     try:
#         f.close()
#     except:
#         print('文件不存在，请先创建文件')

#  使用with后不管with中的代码出现什么错误，都会进行对当前对象进行清理工作。
#
# 例如file的file.close()方法，无论with中出现任何错误，都会执行file.close（）方法
with open(r'aa.txt','r') as f:
    for line in f:
        print(f.readline())