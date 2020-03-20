# 测试@property的简单用法

# class Employee:
#     @property
#     def salary(self):
#         print("salary run....")
#         return 10000
# emp=Employee()
# #加上@property时，可以把方法当做变量一样，不用加括号也行
# print(emp.salary)
# #但是仅仅有 @property 是不能给salary赋值
# #emp.salary=19

# 用get set 方法实现对私有的访问及改变
# class Employee:
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary
#     def get_salary(self):
#         return self.__salary
#     def set_salary(self,salary):
#         if 1000<salary<222222:
#             self.__salary=salary
#         else:
#             print("输入错误")
#
# e1 = Employee("liu", 100000)
# print(e1.get_salary())
# e1.set_salary(2000003)
# print(e1.get_salary())


# 用装饰器实现对私有的调用及改变(代替get set方法)
#可以赋值了
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary2(self):
        return self.__salary

    @salary2.setter
    def salary1(self, salary):
        if 1000 < salary < 222222:
            self.__salary = salary
        else:
            print("输入错误")


e2 = Employee("lin", 1200)
print(e2.salary2)
# e2.salary1 = 1211
# print(e2.salary2)
