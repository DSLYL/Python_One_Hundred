"""开发画图软件的菜单
"""
from tkinter.filedialog import *
from tkinter.colorchooser import *

win_width = 500
win_height = 300


class Application(Frame):

    def __init__(self, master=None,bgcolor="#000000"):
        super().__init__(master)        # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.x = 0
        self.y = 0
        self.lastDraw = 0    #最后一条直线的id
        self.fgcolor = "#ff0000"
        self.pack()
        self.startDrawFlag = False
        self.bgcolor = bgcolor
        self.createWidget()
        root.bind("<KeyPress-r>",self.kuaijiejian)
        root.bind("<KeyPress-y>",self.kuaijiejian)
        root.bind("<KeyPress-g>",self.kuaijiejian)

    def createWidget(self):
        # 绘图区
        self.c = Canvas(root, width=win_width, height=win_height*0.8, bg=self.bgcolor)
        self.c.pack()
        # 创建按钮
        btn_start = Button(root, text="开始", name="start")
        btn_start.pack(side="left", padx="10")
        btn_pen = Button(root, text="画笔", name="pen")
        btn_pen.pack(side="left", padx="10")
        btn_rect = Button(root, text="矩形", name="rect")
        btn_rect.pack(side="left", padx="10")
        btn_clear = Button(root, text="清屏", name="clear")
        btn_clear.pack(side="left", padx="10")
        btn_erasor = Button(root, text="橡皮擦", name="erasor")
        btn_erasor.pack(side="left", padx="10")
        btn_line = Button(root, text="直线", name="line")
        btn_line.pack(side="left", padx="10")
        btn_lineArrow = Button(root, text="箭头直线", name="lineArrow")
        btn_lineArrow.pack(side="left", padx="10")
        btn_color = Button(root, text="颜色", name="color")
        btn_color.pack(side="left", padx="10")

        #事件处理
        btn_line.bind_class("Button","<1>",self.eventManager)
        self.c.bind("<ButtonRelease-1>", self.stopDraw)
        # btn_lineArrow.bind_class("Button","<1>", self.mylineArrow)

    def eventManager(self, event):
        name = event.widget.winfo_name()
        print(name)
        if name=="line":
            self.c.bind("<B1-Motion>", self.myline)
        elif name=="lineArrow":
            self.c.bind("<B1-Motion>", self.mylineArrow)
        elif name=="rect":
            self.c.bind("<B1-Motion>", self.myRect)
        elif name =="pen":
            self.c.bind("<B1-Motion>", self.myPen)
        elif name =="erasor":
            self.c.bind("<B1-Motion>", self.myErasor)
        elif name =="clear":
            self.c.delete("all")
        elif name == "color":
            c = askcolor(color="#ff0000", title="选择画笔颜色")
            self.fgcolor = c[1]
    def stopDraw(self, event):
        self.startDrawFlag = False
        self.lastDraw = 0         #值为0或负数，代表值不存在，故找不到删除的点

    def startDraw(self, event):
        self.c.delete(self.lastDraw)
        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y
    def myline(self, event):
        self.startDraw(event)
        self.lastDraw = self.c.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
    def mylineArrow(self, event):
        self.startDraw(event)
        self.lastDraw = self.c.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fgcolor)
    def myRect(self,event):
        self.startDraw(event)
        self.lastDraw = self.c.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)

    def myPen(self,event):
        self.startDraw(event)
        self.c.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
        self.x = event.x
        self.y = event.y
    # 画笔和橡皮擦的原理类似
    def myErasor(self, event):
        self.startDraw(event)
        self.c.create_rectangle(event.x-10, event.y-10,event.x, event.y, fill=self.bgcolor)
    def kuaijiejian(self,event):
        if event.char =="r":
            self.fgcolor = "#ff0000"        #红色
        elif event.char =="g":
            self.fgcolor = "#00ff00"        #绿色
        elif event.char =="y":
            self.fgcolor = "#ffff00"        #黄色
if __name__ == '__main__':
    root = Tk()
    root.geometry(str(win_width)+"x"+str(win_height)+"+200+300")
    root.title("百战程序员的简易画图本")
    app = Application(master=root)
    root.mainloop()