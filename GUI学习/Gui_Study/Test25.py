from tkinter.filedialog import *



root = Tk();root.geometry("400x400")
#创建主菜单栏
menubar = Menu(root)
#创建子菜单
menuFile = Menu(menubar)
menuEdit = Menu(menubar)
menuHelp = Menu(menubar)
#把子菜单加入到主菜单栏
menubar.add_cascade(label="文件（E）", menu=menuFile)
menubar.add_cascade(label="编辑（E）", menu=menuEdit)
menubar.add_cascade(label="帮助（H）", menu=menuHelp)
filename = ""

def openfile():
    global filename
    w1.delete('1.0', 'end')
    with askopenfile(title="打开文件") as f:
        content = f.read()
        w1.insert(INSERT, content)
        filenmae = f.name
        print(f.name)
def savefile():
    with open(filename, 'w') as f:
        content = w1.get(1.0, END)
        f.write(content)

def exit():
    root.quit()


menuFile.add_command(label="打开", accelerator="crtl+o", command=openfile)
menuFile.add_command(label="保存", command=savefile)
menuFile.add_separator()
menuFile.add_command(label="退出", command=exit)

root["menu"] = menubar




w1 = Text(root, width=50, height=30)
w1.pack()
root.mainloop()


