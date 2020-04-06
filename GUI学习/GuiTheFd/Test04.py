from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    def createWidget(self):
        # anchor 代表text 在button中的位置
        self.btn01 = Button(root, text="登录", width=6, height=3, anchor=E, command=self.login)
        self.btn01.pack()

        global photo
        photo = PhotoImage(file="imgs/start.gif")
        self.btn02 = Button(root, image=photo, command=self.login)
        self.btn02.pack()



    def login(self):
        messagebox.showinfo("Message:","刘芸隆在写代码，不是吗")
if __name__ == '__main__':
    root = Tk()
    root.geometry("400x400+200+250")
    app = Application(master=root)
    root.mainloop()