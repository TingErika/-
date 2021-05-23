#coding=utf-8
# @Author: chenyuanzhe
# @Time: 2021-04-10 15:32
# @Abstract：简单线性回归（Simple Linear Regression）算法预测油气产量
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
from matplotlib import rc
rc('mathtext', default='regular')

datapath=r"D:\迅雷下载\毕业设计\算法\Russia.csv"
deliveryData = genfromtxt(datapath,delimiter=',')
datapath2=r"D:\迅雷下载\毕业设计\算法\Saudi Arabia.csv"
deliveryData2 = genfromtxt(datapath2,delimiter=',')

# 读取自变量X1(运送英里数),X2(运送次数)
x= deliveryData[1:,0]
# 读取因变量(运送时间)
y = deliveryData[1:,1]
z = deliveryData[1:,2]
y2 = deliveryData2[1:,1]
z2 = deliveryData2[1:,2]

print("y:",y)
print("z:",z)

fig = plt.figure()
ax = fig.add_subplot(111)

lns1=ax.plot(x, y, '-', label = 'Luminous(Russia)')
lns3=ax.plot(x, y2, '-c', label = 'Luminous(Saudi Arabia)')
ax2 = ax.twinx()
lns2=ax2.plot(x, z, '-r', label = 'Oil Production(Russia)')
lns4=ax2.plot(x, z2, '-m', label = 'Oil Production(Saudi Arabia)')

lns=lns1+lns2+lns3+lns4
labs=[l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)

ax.set_xlabel("Year")
ax.set_ylabel("Luminous (nanoWatts)")
ax2.set_ylabel("Oil Production (Barrels)")
plt.show()




