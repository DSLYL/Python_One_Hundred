# from tkinter import *
#
# root = Tk();root.geometry("500x500")
# def mouseTest1():
#     print("啊啊啊啊")
#
# def mouseTest2(a, b):
#     print("a={0},b={1}".format(a, b))
#
# Button(root, text="测试command1", command=mouseTest1).pack(side="left")
#
# Button(root, text="测试2", command=lambda: mouseTest2("liu", "yunLong")).pack(side="left")
#
#
# root.mainloop()

a = lambda x, y, z: x + y + z
print(a(1, 2, 3))
a1 = lambda *args: sum(args)
print(a1(1, 23, 3, 32, 1))
