from tkinter import *
from tkinter.colorchooser import *

root = Tk();root.geometry("500x500")

def test1():
    s1 = askcolor(color="red", title="选择背景颜色")
    print(s1)
    root.config(bg=s1[1])


Button(root, text="选择背景颜色", command=test1).pack()
root.mainloop()