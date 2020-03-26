# 请编写程序，生成随机密码。具体要求如下：
# 使用random库，采用0x1010作为随机数种子。
# 密码由26个字母大小写、10个数字字符和!@#$%^&*等8个特殊符号组成。
# 每个密码长度固定为10个字符。
# 程序运行每次产生10个密码，每个密码一行。
# 每次产生10个密码首字符不能一样。
# 程序运行后产生的密码保存在“随机密码.txt”文件中。

import random

random.seed(0x1010)
s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678910!@#$%^&*'
ls = []
e = ""  # 存储首字母
while len(ls) < 10:
    pwd = ""
    for i in range(10):
        pwd += s[random.randint(0, len(s))]
    if pwd[0] in e:
        continue
    else:
        ls.append(pwd)
        e += pwd[0]
fo = open(r'随机密码.txt', 'w')
fo.write("\n".join(ls))
fo.close()
