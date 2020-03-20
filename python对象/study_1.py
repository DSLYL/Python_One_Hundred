# 测试方法的动态性
class Person:
    def work(self):
        print("努力学习")


def play_game(s):
    print("{0}在玩游戏".format(s))


def work(s):
    print("sdfa{0}".format(s))


Person.play = play_game
p = Person()
p.work()
Person.work1 = work
p.work1()

# 下面这个是不对的
# p.play_game()
# 下面能运行了，原因：Person.paly=play_game （是把play_game的地址给了前者 play）
# 而p.play()的意思是Person.play(p),所以打印出的是  对象p 在玩游戏
p.play()

#方法是对象  函数是对象 一切都是对象
