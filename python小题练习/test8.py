# 输入某年某月某日，判断这一天是这一年的第几天？

# import datetime
#
# y = int(input('请输入4位数字的年份：'))  # 获取年份
# m = int(input('请输入月份：'))  # 获取月份
# d = int(input('请输入是哪一天：'))  # 获取“日”
#
# targetDay = datetime.date(y, m, d)  # 将输入的日期格式化成标准的日期
# print(targetDay - datetime.date(targetDay.year - 1, 12, 31))  # 减去上一年最后一天，可得解
import datetime

y = int(input('请输入4位数字的年份：'))  #获取年份
m = int(input('请输入月份：'))  #获取月份
d = int(input('请输入是哪一天：'))  #获取“日”

targetDay = datetime.date(y, m, d)  #将输入的日期格式化成标准的日期
dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31)  #减去上一年最后一天

print('{0}是{1}年的第{2}天'.format(targetDay, y, dayCount.days))
