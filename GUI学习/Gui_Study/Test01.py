from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('我的第一个GUI程序')
root.geometry("500x300+100+200")

btn01 = Button(root)
btn01["text"] = "点我送花"
btn01.pack()


def songhua(e):  # e就是事件对象
    messagebox.showinfo("送你花，开心吧ds fasf as ")
    print("送你99朵呦")


btn01.bind("<Button-1>", songhua)
root.mainloop()
