from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.btn01 = Button(self)
        self.btn01["text"] = "点击送花"
        self.btn01.pack()
        self.btn01["command"] = self.songhua
        # 创建一个退出按钮
        self.btnQuit = Button(self, text="退出", command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("Message", "送花啦啦")


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500+300+300")
    root.title("第二个GUI程序")
    app = Application(master=root)
    root.mainloop()
