#CSV读取学习
import  csv
with open(r"ee.csv","r") as f:
    r1=csv.reader(f)
    print(r1)
    # print(list(r1))
    for i in r1:
        print(i)