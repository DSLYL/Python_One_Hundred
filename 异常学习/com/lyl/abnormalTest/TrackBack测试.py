# 测试trackback模块
#
# import traceback
#
# try:
#     print('step1')
#     a = 1/0
# except:
#     # 下面这个是可以正常打印错误提示
#     traceback.print_exc()
#

#########把异常信息写入文件中

import  traceback

try:
    print('11')
    a = 1/0
except:
    with open(r'C:\Users\Administrator\Desktop/aa.txt','a+') as f:
            traceback.print_exc(file=f)