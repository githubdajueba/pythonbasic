#!/usr/bin/python
# -*- coding: utf-8 -*-

# import  tensorflow as tf
#
# print(tf.__version__)
import pandas as pd
#import matplotlib.pyplot as pit
# data = pd.read_csv("./data.csv")
# x = data.Excution
import tensorflow as tf
import matplotlib.pyplot as plt

# 通过pd读取文件
data = pd.read_csv('./data.csv')
x = data.Education
y = data.Income
# 通过plt绘制图像
plt.scatter(x, y)
# plt.show()

# 顺序模型&序贯模型初始化 包括一次函数,无网络结构
model = tf.keras.Sequential()
# 可以使用Sequential(有_init_方法)的构造函数,或者继续model.add()来增加层数
# 传入Dense层,指定输出维度为1 输入维度为1  .Dense 一次函数
#  输出一个  输入x,y
model.add(tf.keras.layers.Dense(1, input_shape=(1,)))
# 展示模型
# model.summary()

# 创建模型,指定优化器和损失函数 adam-优化算法 算是函数-均方差
model.compile(optimizer='adam', loss='mse')
# 保留训练过程,指定训练数据和训练次数,并得到最终模型.此时model已经保存了训练完毕的模型.
history = model.fit(x, y, epochs=50000)

# # 使用训练完毕的模型预测数据得到预测结果
x1 = x
y1 = model.predict(x)

# 讲预测结果绘制为图像用于对比原数据,评估契合度
plt.scatter(x1, y1)
plt.show()

# 预测在受教育年限为6,9,12,16,20年时,薪资水平分别是多少
fx = model.predict([6, 9, 12, 16, 20])
print(fx)




"""
 y = ax+b+0
 噪声:纵轴上的距离
 穿过的点最多,噪声值最小
 y-ax-b=0
 loss 0=求和|yi-(axi+b)|
 但绝对值不常用,可以用整个的平方,再求和
 还可以处以 n,让数变小
 loss 0 损失函数
mse= 均方差公式
 
 梯度下降
 导数:
 偏导:有多个自变量时,只求一个的导数
 斜率:正 --上坡
     负--下降
y = f(x)
x=x-d(斜率)*0.0000x
可以用随机多个x同时计算

找到最小值  
   
 
 
"""