while True:
    x = input('Please input:')
    try:
        x = int(x)
        # print("you have input{0}".format(x))
        break
    except BaseException as e:
        print(e)
        print(type(e))
        print('Error')

# print('step0')
# try:
#     print('step1')
#     a = 3/0
#     print('step2')
# except:
#     print('发生异常')
# print('end~!!!!')

try:
    a = input('输入被除数')
    b = input('输入除数')
    c = float(a) / float(b)
    print(c)
except ZeroDivisionError:
    print('异常，不能除0')
except ValueError:
    print('异常，不能将字符串转换为数字')
except NameError:
    print('异常，变量不存在')
except BaseException as e:
    print(e)

