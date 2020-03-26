#csv文件写入学习
import  csv
headers = ["工号","姓名","年龄","地址","月薪"]
rows = [("1001","高淇",18,"西三旗 1 号院","50000"),("1002","高八",19,"西三旗 1 号院","30000")]
with open(r"ee.csv","w") as f:
    r=csv.writer(f)
    r.writerow(headers)
    r.writerows(rows)
