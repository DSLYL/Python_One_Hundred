#测试canvas
from tkinter import *
from tkinter import messagebox
import random


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master=root)
        self.master = master
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.canvas = Canvas(self, width=400, height=400, bg="green")
        self.canvas.pack()
        #画直线
        # line = self.canvas.create_line(50, 50, 100, 100)
        #画折线
        line1 = self.canvas.create_line(50, 50, 100, 50, 200, 200)
        #画矩形
        rect = self.canvas.create_rectangle(50, 50, 100, 100)
        #画椭圆
        oval = self.canvas.create_oval(200, 50, 100, 100)
        global photo
        photo = PhotoImage(file="imgs/logo.gif")
        self.canvas.create_image(200, 300, image=photo)
        Button(self, text="画10个圆", command=self.drawCircle).pack(side="left")
        ""
    def drawCircle(self):
        for i in range(0, 10):
            x1 = random.randrange(int(self.canvas["width"])/2)
            y1 = random.randrange(int(self.canvas["height"])/2)
            x2 = x1 + random.randrange(int(self.canvas["width"])/2)
            y2 = y1 + random.randrange(int(self.canvas["height"])/2)
            self.canvas.create_oval(x1, y1, x2, y2 )

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500+200+200")
    app = Application(master=root)
    root.mainloop()
