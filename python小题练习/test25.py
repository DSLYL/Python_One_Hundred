# 编写一个while 循环,提示用户输入其名字。
# 用户输入其名字后,在屏幕上打印一句问候语,并将一条访问记录添加到文件guest_book.txt中。
# 确保这个文件中的每条记录都独占一行。此外设置当输入q时停止本程序。

# def fun():
#     while(True):
#         print("Please input your name:")
#         a = input()
#         print("hi,are you ok?")
#         with open(r"guest_book.txt",'a+') as f:
#             f.write(a+'\n')
#         if a=='q':
#             break
# fun()

filename='guest_book.txt'
# 如果有引号，单双进行交替
guest_name=input('Please input your name: (input "q" to quit )')
while guest_name!='q':
    with open(filename,'a') as f:
        f.write(guest_name+'\n')
    guest_name = input("Please input your name: (input 'q' to quit )")