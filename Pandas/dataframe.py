# !/usr/bin/env python
# encoding: utf-8
__author__ = 'Administrator'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#一、创建对象
#1. 通过传递一个list对象来创建一个Series，pandas会默认创建整型索引：
s=pd.Series([1,3,4,np.nan,6,8])
print(s)
# 0    1.0
# 1    3.0
# 2    4.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64

#2.通过传递一个numpy array，时间索引以及列标签来创建一个DataFrame：
dates=pd.date_range('20180301',periods=6)
print(dates)
# DatetimeIndex(['2018-03-01', '2018-03-02', '2018-03-03', '2018-03-04',
#                '2018-03-05', '2018-03-06'],
#               dtype='datetime64[ns]', freq='D')
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
# numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。(可含负数）
# numpy.random.rand(d0, d1, …, dn)的随机样本位于[0, 1)中。
#P=numpy.random.rand(N,K) #随机生成一个 N行 K列的矩阵
print(df)
#                    A         B         C         D
# 2018-03-01 -0.451506 -0.884044 -0.916664 -0.763684
# 2018-03-02 -0.463568  0.340688 -0.077484 -0.237660
# 2018-03-03 -1.533427  0.301283  0.268640 -0.011027
# 2018-03-04  1.036050  0.402203  0.485365  2.086525
# 2018-03-05  0.221578 -0.821756 -0.265241  0.277563
# 2018-03-06  1.774195 -0.288553  1.527936  0.119153

#3.通过传递一个能够被转换成类似序列结构的字典对象来创建一个DataFrame：
df2=pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20180301'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(["test","train","test","train"]),
    'F':'foo'})
print(df2)
#      A          B    C  D      E    F
# 0  1.0 2018-03-01  1.0  3   test  foo
# 1  1.0 2018-03-01  1.0  3  train  foo
# 2  1.0 2018-03-01  1.0  3   test  foo
# 3  1.0 2018-03-01  1.0  3  train  foo

#4.查看不同列的数据类型：
print(df2.dtypes)
# A           float64
# B    datetime64[ns]
# C           float32
# D             int32
# E          category
# F            object
# dtype: object

#二、查看数据
#1. 查看dataframe中头部和尾部的行：
print(df.head())
#                    A         B         C         D
# 2018-03-01 -0.250132 -1.403066  1.234990 -3.077763
# 2018-03-02  0.387496 -0.389183  0.186663  1.124608
# 2018-03-03 -0.105463 -0.230739 -0.227575  0.308565
# 2018-03-04 -1.703507  0.194876  1.790366 -0.561566
# 2018-03-05 -0.511609  0.695915  0.398392  0.107062
print(df.tail(3))
#                    A         B         C         D
# 2018-03-04  0.704065  0.492649  0.533961 -1.518723
# 2018-03-05  2.192819 -0.508099 -0.173966 -0.401864
# 2018-03-06 -0.839634 -0.314676 -0.808266 -0.578229

#2.显示索引、列和底层的numpy数据：
print(df.index)
# DatetimeIndex(['2018-03-01', '2018-03-02', '2018-03-03', '2018-03-04',
#                '2018-03-05', '2018-03-06'],
#               dtype='datetime64[ns]', freq='D')
print(df.columns)
#Index(['A', 'B', 'C', 'D'], dtype='object')
print(df.values)
# [[ 1.65612186 -0.47932887  0.9673593  -0.63872414]
#  [ 0.12229686  0.08831358  1.07344126 -0.12742276]
#  [ 0.54654075  0.77281164 -0.6396787   0.1585142 ]
#  [-0.70695944 -2.12273423 -0.24549759 -0.09530991]
#  [ 2.66920788  0.6520858   1.72857641 -1.34418643]
#  [ 1.87333346 -0.42716996  0.49558928 -1.47606701]]

