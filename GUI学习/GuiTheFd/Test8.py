from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        super.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        #用来存放onvalue  offvalue的值
        self.codeHobby = IntVar()
        self.videoHobby = IntVar()

        # print(self.codeHobby.get())
        self.c1 = Checkbutton(self, text="敲代码", variable=self.codeHobby, onvalue=1, offvalue=0)
        self.c2 = Checkbutton(self, text="看电视剧", varibale=self.videoHobby, onvalue=1, offvalue=0)
        self.c1.pack(side="left")
        self.c2.pack(side="left")
        Button(self, text="确定", command=self.confirm).pack(side="left")
    def confirm(self):
        if self.videoHobby.get() == 1:
            messagebox.showinfo("测试：", "看视频打发时间")
        if self.codeHobby.get() == 1:
            messagebox.showinfo("测试：", "写代码可以进步")
if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500+400+400")
    app = Application(master=root)
    root.mainloop()
