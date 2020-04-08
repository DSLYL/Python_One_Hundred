from tkinter import *


root = Tk();root.geometry("700x220")
f1 = Frame(root)
f1.pack()
f2 = Frame(root);f2.pack()

btnText = ("流行歌曲", "中国风", "英语歌曲", "二人转", "日本风")
for txt in btnText:
    Button(f1, text=txt).pack(side="left", padx="10")

for i in range(1,12):
    Label(f2, width=5, height=10, borderwidth=1,relief="solid",
          bg="black" if i%2==0 else "white").pack(side="left", padx=2)

root.mainloop()
