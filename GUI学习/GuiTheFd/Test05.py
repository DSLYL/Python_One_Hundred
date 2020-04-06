from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.label01 = Label(self,text="用户名")
        self.label01.pack()
        v1 = StringVar()
        self.entry01 = Entry(self,textvariable = v1)
        self.entry01.pack()
        v1.set("admin")
        print(v1.get());print(self.entry01.get())

    #     创建密码框：
        self.label02 = Label(self,text="密码")
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.pack()
        Button(self, text="登录",command=self.login).pack()




    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()
        print("用户名："+username)
        print("密码："+pwd)
        # 考虑一下，为什么有了else才可以执行？
        if username=="yunlong" and pwd=="123456":
            messagebox.showinfo("Message:","刘芸隆在写代码，不是吗")
        else:
            messagebox.showinfo("Message:", "输入错误")
if __name__ == '__main__':
    root = Tk()
    root.geometry("400x400+200+250")
    app = Application(master=root)
    root.mainloop()