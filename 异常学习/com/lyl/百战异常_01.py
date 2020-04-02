# 写一个读写文件的程序，并且加入异常



import  traceback
try:
    with open(r'e.txt','a+') as f:
        f.write('123'+'\n')
        f.write('234')
        f.write('asdf')
        f.write(23)
except:
    print('f')
