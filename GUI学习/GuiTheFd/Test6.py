from tkinter import*
import tkinter.font as f
import webbrowser

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.w1 = Text(root, width=40, height=12, bg="gray", fg="black")
        self.w1.pack()

        self.w1.insert(1.0, "01234556\nabcdefg")
        self.w1.insert(2.3, "写代码的日子很长， 继续加油，努力")
        Button(self, text="重复插入文本", command=self.insertText).pack(side="left")
        Button(self, text="返回文本", command=self.returnText).pack(side="left")
        Button(self, text="添加图片", command=self.addImage).pack(side="left")
        Button(self, text="添加组件", command=self.addWidget).pack(side="left")
        Button(self, text="通过tag精通控制文本", command=self.testTag).pack(side="left")
    def insertText(self):
        #INSERT代表 在光标处插入
        self.w1.insert(INSERT, "刘芸隆")
        self.w1.insert(END, '[zbdx]')
        self.w1.insert(1.8, "加油！！")
    def returnText(self):
        print(self.w1.get(1.2, 1.6))
        print("文本所有内容：\n"+self.w1.get(1.0, END) )

    def addImage(self):
        self.photo = PhotoImage(file="imgs/logo.gif")
        self.w1.image_create(END, image=self.photo)
    def addWidget(self):
        b1 = Button(self.w1, text="我要努力！！")
        self.w1.window_create(INSERT, window=b1)
    def testTag(self):
        self.w1.delete(1.0, END)
        self.w1.insert(INSERT, "nice,nice\n我要成功，我要加油！！，我是最棒的！！\nbaidu")
        self.w1.tag_add("nice", 1.0, 1.9)
        self.w1.tag_config("nice", background="red", foreground="black")
        self.w1.tag_add("baidu", 3.0, 3.5)
        self.w1.tag_config("baidu", underline=True)
        self.w1.tag_bind("baidu", "<Button-1>", self.webshow)

    def webshow(self, event):
        webbrowser.open("http://www.baidu.com")

if __name__ == '__main__':
    root = Tk()

    root.geometry("400x500+200+200")
    app = Application(master=root)
    root.mainloop()