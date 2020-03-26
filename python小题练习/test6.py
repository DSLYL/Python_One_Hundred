# import turtle
# import time
#
# turtle.showturtle()
# turtle.left(30)
# turtle.forward(100)
# for i in range(5):
#     turtle.right(60)
#     turtle.forward(100)
# time.sleep(2)



#棋盘绘制


# import turtle
#
# t = turtle.Pen()
# t.width(2)
# t.speed(100)
# # 绘制竖线
# for x in range(11):
#     t.penup()
#     t.goto(x * 30, 0)
#     t.pendown()
#     t.goto(x * 30, -300)
#
# # 绘制横线
# for x in range(11):
#     t.penup()
#     t.goto(0, -x * 30)
#     t.pendown()
#     t.goto(300, -x * 30)
#
# t.hideturtle()  # 隐藏画笔
# turtle.done()  # 使窗口不自动关闭

import turtle

t = turtle.Pen()
t.hideturtle()     #隐藏箭头
t.speed(100)
#棋盘由横线和竖线组成，主要是控制好它们的数量。
#横线
for m in range(0, 19):
    #回来的时候避免画线，所以抬笔
    t.penup()
    #20是棋格的宽度
    t.goto(0, m * 20)
    t.pendown()
    t.goto(360, m * 20)
#竖线
for n in range(0, 19):
    t.penup()
    t.goto(n * 20, 0)
    t.pendown()
    t.goto(n * 20, 360)

turtle.done()  # 使窗口不自动关闭