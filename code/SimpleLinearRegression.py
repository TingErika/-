#coding=utf-8
# @Author: chenyuanzhe
# @Time: 2021-04-10 15:32
# @Abstract：简单线性回归（Simple Linear Regression）算法预测油气产量
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

datapath=r"D:\迅雷下载\毕业设计\算法\Iraq.csv"
deliveryData = genfromtxt(datapath,delimiter=',')

# 读取自变量X1(运送英里数),X2(运送次数)
x= deliveryData[1:,1]
# 读取因变量(运送时间)
y = deliveryData[1:,2]

print("x:",x) 
print("y:",y) 

def fitSLR(x, y):
    n = len(x)
    dinominator = 0
    numerator = 0
    for i in range(0, n):
        numerator += (x[i] - np.mean(x)) * (y[i] - np.mean(y))
        dinominator += (x[i] - np.mean(x)) ** 2

    print("numerator:" + str(numerator))
    print("dinominator:" + str(dinominator))

    a = numerator / float(dinominator)
    b = np.mean(y) - a * float(np.mean(x))

    return a, b

# y= a*x+b
def prefict(x, a, b):
    return a * x + b

a, b = fitSLR(x, y)
y_predict = prefict(56229632.04, a, b)
print("y_predict:" + str(y_predict))

plt.xlabel("Luminous (nanoWatts)")
plt.ylabel("Oil Production (Barrels)")
plt.scatter(x,y,s=10,c='blue',label='train')
plt.plot(x,a*x+b,c='red',label='predict')
plt.legend()
plt.show()




