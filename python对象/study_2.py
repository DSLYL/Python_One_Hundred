# 测试私有属性
# 在变量或方法前面加上__（俩个下划线）的时候，就成为私有方法或私有变量，
# 要想在类外访问它们，必须使用对象名._类名__变量名或方法名
#访问私有类变量时，是  类名._类名__变量名
#私有的  在类内是可以随意调用的
class Student:
    __Teacher=1   #私有类变量
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def __work(self):
        print("加油！")
        print(self.__age)


e = Student("lui", 23)
print(e.name)
#下面2个是不对的
# print(e.__age)
# print(e.__work())

print(e._Student__age)
e._Student__work()
print(Student._Student__Teacher)

#下面这个打印出变量和方法在内存中的存储名字
print(dir(e))
