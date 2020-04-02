# 结合Matplotlib与numpy绘制函数f(x)=sin2(x-2)e-x2

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ['SimHei']  # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x = np.linspace(-2.5, 2, endpoint=True)  # 绘制X轴（-2.5,2）的图像

f = (np.sin(x - 2)) ** 2 * (np.e) ** (-x ** 2)  # y值

plt.plot(x, f, "g-", lw=2.5, label="f(x)")
plt.title('f(x) = sin^2(x-2)e^{-x^2}函数图')
plt.legend()
plt.show()



