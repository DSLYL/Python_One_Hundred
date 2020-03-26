import pickle

# 先将对象序列化到文件中
# with open(r"bb.dat","wb") as f:
#     a1='是的'
#     a2=123
#     a3=[1,23,4]
#     pickle.dump(a1,f)
#     pickle.dump(a2, f)
#     pickle.dump(a3, f)

# 将获得的数据反序列化成对象
with open(r"bb.dat", "rb") as f:
    a1 = pickle.load(f)
    a2 = pickle.load(f)
    a3 = pickle.load(f)
    print(a1)
    print(a2)
    print(a3)
