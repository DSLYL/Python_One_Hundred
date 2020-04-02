# import numpy as np
# a=np.zeros([10]*2)
# a[[0,-1],:]=1
# a[:,[0,-1]]=1
# print(a)


import numpy as np

z=np.ones((10,10))
z[1:-1,1:-1] = 0
print(z)

