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
        #给标签上面写内容，也可以
        #self.label01["text"] = "刘芸隆"
        self.label01 = Label(self, text="刘芸隆", width=6, height=2, bg="black", fg="white")
        self.label01.pack()

        self.label02 = Label(self, text="北京大学", width=8, height=5, bg="yellow", fg="white", font=("宋体", 30))

        # 上面的代码和下面的类似
        # self.label02 = Label(self, text="北京大学", width=8, height=5, font=("宋体", 30))
        # self.label02.config(bg="blue", fg="red")
        self.label02.pack()

        global photo
        photo = PhotoImage(file="imgs/logo.gif")
        self.label03 = Label(self,image=photo)
        self.label03.pack()

        self.label04 = Label(self,text="中北大学\n刘芸隆\n喜欢写代码\n喜欢枪类游戏", borderwidth=11, relief="groove", justify="left")
        self.label04.pack()


    def songhua(self):
        messagebox.showinfo("Message", "送花啦啦")


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500+300+300")
    root.title("第二个GUI程序")
    app = Application(master=root)
    root.mainloop()
