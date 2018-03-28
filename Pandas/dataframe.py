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

'''

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

#3. describe()函数对于数据的快速统计汇总：
print(df.describe())
#               A         B         C         D
# count  6.000000  6.000000  6.000000  6.000000
# mean   0.399068  0.339270  0.755588 -0.459344
# std    0.890360  1.011113  0.851783  1.759264
# min   -1.002101 -0.806772 -0.333761 -2.411582
# 25%   -0.087757 -0.400563  0.338822 -1.782221
# 50%    0.577418  0.244011  0.502612 -0.622453
# 75%    1.096592  0.941454  1.376095  0.433235
# max    1.281508  1.795854  1.910586  2.284103

#4. 对数据的转置：
print(df.T)
#    2018-03-01  2018-03-02  2018-03-03  2018-03-04  2018-03-05  2018-03-06
# A    0.843347   -0.906826   -0.528945    1.186650   -1.839152   -0.508169
# B   -0.105481    2.084689   -1.106710    0.521137    0.741946    0.399700
# C   -0.786144    0.269116   -0.180710    3.345385    1.310786   -0.204216
# D    0.453731   -0.243617    0.701440    2.541094    1.337923   -0.673128

#5. 按轴进行排序
print(df.sort_index(axis=1,ascending=False)) #  axis = 0是按行进行操作, axis=1是按列进行操作;  ascending=False是只递减，否则递增
#                    D         C         B         A
# 2018-03-01  0.389294 -0.227394  0.649234  0.639820
# 2018-03-02  0.680265  0.466626 -1.940228  0.843753
# 2018-03-03  1.520800  0.570192  1.244427 -0.715080
# 2018-03-04  0.309068 -0.224222 -0.226254  1.416381
# 2018-03-05 -1.854131 -0.403245 -0.017054  0.840840
# 2018-03-06 -1.991173  1.275825  0.913996  1.561550

#6. 按值进行排序
# print(df.sort(column='B')) #?? AttributeError: 'DataFrame' object has no attribute 'sort'

#三、选择
# 虽然标准的Python/Numpy的选择和设置表达式都能够直接派上用场，
# 但是作为工程使用的代码，我们推荐使用经过优化的pandas数据访问方式： .at, .iat, .loc, .iloc 和 .ix
#（一）获取：
#1. 选择一个单独的列，这将会返回一个Series，等同于 df.A：
print(df['A'])
# 2018-03-01    0.156236
# 2018-03-02   -0.041257
# 2018-03-03   -0.970551
# 2018-03-04   -1.751839
# 2018-03-05    1.521352
# 2018-03-06    0.828690
# Freq: D, Name: A, dtype: float64

#2. 通过[]进行选择，这将会对行进行切片
print(df[0:3])
#                    A         B         C         D
# 2018-03-01 -0.432011  0.697033 -3.028116 -0.217882
# 2018-03-02 -1.744071  0.647694  1.031179 -1.043985
# 2018-03-03 -0.673125  0.689913  0.648986 -1.471825
print(df['20180302':'20180304'])
#                    A         B         C         D
# 2018-03-02 -0.803947  0.147807 -0.248534  0.496719
# 2018-03-03 -1.518123  0.376390 -0.793349  0.612074
# 2018-03-04  0.146634  0.506102  1.316693 -0.801691

#（二）通过标签选择：
#1. 使用标签来获取一个交叉的区域：
print(df.loc[dates[0]])
# A   -1.593039
# B    0.400735
# C   -0.870638
# D   -0.551766
# Name: 2018-03-01 00:00:00, dtype: float64
#2. 通过标签来在多个轴上进行选择：
print(df.loc[:,['A','B']])
#                    A         B
# 2018-03-01  0.326446  0.633246
# 2018-03-02  0.169674  0.892832
# 2018-03-03 -0.755691 -2.028912
# 2018-03-04 -1.005360  0.529193
# 2018-03-05 -0.457140  0.842211
# 2018-03-06  0.343157  0.879763

#3. 标签切片
print(df.loc['20180302':'20180304',['A','B']])
#                    A         B
# 2018-03-02  0.197173  0.040377
# 2018-03-03  2.064367  1.112152
# 2018-03-04  0.888216 -0.591129

#4. 对于返回的对象进行维度缩减
print(df.loc['20180302',['A','B']])
# A   -0.259955
# B   -0.019266
# Name: 2018-03-02 00:00:00, dtype: float64

#5. 获取一个标量
print(df.loc[dates[0],'A']) #-0.313259346223

#6. 快速访问一个标量（与上一个方法等价）
print(df.at[dates[0],'A'])  #-0.313259346223

#（三）通过位置选择：
#1. 通过传递数值进行位置选择（选择的是行）
print(df.iloc[3])
# A    1.661488
# B   -1.175748
# C    0.642823
# D   -0.491914
# Name: 2018-03-04 00:00:00, dtype: float64

#2. 通过数值进行切片，与numpy/python 中的情况类似
print(df.iloc[3:5,0:2])
#                    A         B
# 2018-03-04  0.492426  0.412712
# 2018-03-05  0.541252 -0.009380

#3. 通过制定一个位置的列表，与numpy/python中的情况类似
print(df.iloc[[1,2,4],[0,2]])
#                    A         C
# 2018-03-02 -0.638074  1.794516
# 2018-03-03 -0.403471 -0.934373
# 2018-03-05 -1.309320  1.353276

#4. 对行进行切片
print(df.iloc[1:3,:])
#                    A         B         C         D
# 2018-03-02  1.980513 -0.218688  2.627449  1.314947
# 2018-03-03 -0.532379  1.382092 -1.270961  0.722475

#5. 对列进行切片
print(df.iloc[:,1:3])
#                    B         C
# 2018-03-01  0.332228 -1.682811
# 2018-03-02 -0.533398 -0.254960
# 2018-03-03 -0.926688  0.890513
# 2018-03-04 -0.448742  0.763850
# 2018-03-05 -0.841622  0.514873
# 2018-03-06 -1.346557  1.516414

#6. 获取特定的值
print(df.iloc[1,1]) #0.481882236461
print(df.iat[1,1]) #0.481882236461



#（四）布尔索引：
#1. 使用一个单独列的值来选择数据：
print(df[df.A>0])
#                    A         B         C         D
# 2018-03-02  0.566243  1.510954 -0.898180  0.856439
# 2018-03-03  1.008447 -1.597226 -0.665134 -0.287472
# 2018-03-05  0.952498 -0.144979  0.620468 -0.830652

#2. 使用where操作来选择数据：
print(df[df>0])
#                    A         B         C         D
# 2018-03-01  0.892660       NaN       NaN       NaN
# 2018-03-02  1.512600       NaN       NaN  1.375527
# 2018-03-03  0.970026  1.184603  1.182990       NaN
# 2018-03-04  1.913993       NaN  0.914778  0.137170
# 2018-03-05  0.482589       NaN       NaN  0.668817
# 2018-03-06       NaN  0.539344  0.142892       NaN

#3. 使用isin()方法来过滤：
df2=df.copy()
df2['E']=['one','one','two','three','four','three']
print(df2)
#                    A         B         C         D      E
# 2018-03-01 -1.138724  0.566583  0.338254  2.072839    one
# 2018-03-02 -0.366949  0.335546  1.653024  1.445071    one
# 2018-03-03  0.724615  1.715933 -0.754757 -1.452252    two
# 2018-03-04 -0.881962 -0.173858 -0.340868 -0.556665  three
# 2018-03-05 -2.126513 -0.113010 -0.796566  0.210673   four
# 2018-03-06  0.716490  0.223395 -1.428238  0.328406  three
print(df2[df2['E'].isin(['two','four'])])
#                    A         B         C         D     E
# 2018-03-03 -0.737833 -1.161520  0.897204 -0.029158   two
# 2018-03-05  1.072054  1.234587  0.935680 -1.284542  four



#（五）设置：
#1. 设置一个新的列：
s1=pd.Series([1,2,3,4,5,6],index=pd.date_range('20180302',periods=6))
print(s1)
# 2018-03-02    1
# 2018-03-03    2
# 2018-03-04    3
# 2018-03-05    4
# 2018-03-06    5
# 2018-03-07    6
# Freq: D, dtype: int64
df['F']=s1
print(df)
#                    A         B         C         D    F
# 2018-03-01  2.413592 -0.336264  0.165597  2.143270  NaN
# 2018-03-02 -1.921596 -2.100707 -0.454461  0.563247  1.0
# 2018-03-03 -0.235034 -0.517009 -2.409731 -0.711854  2.0
# 2018-03-04  0.667604 -0.838737 -0.425916 -0.238519  3.0
# 2018-03-05  1.057415  1.457143  0.440690  0.948613  4.0
# 2018-03-06  0.539187 -0.952633  0.316752  0.422146  5.0

#2. 通过标签设置新的值：
df.at[dates[0],'A']=0

#3. 通过位置设置新的值：
df.iat[0,1]=0

#4. 通过一个numpy数组设置一组新值：
df.loc[:,'D']=np.array([5]*len(df))
print(df)
#                    A         B         C  D    F
# 2018-03-01  0.000000  0.000000  0.164267  5  NaN
# 2018-03-02  0.614534 -0.865975 -0.977389  5  1.0
# 2018-03-03 -0.253095 -1.451951  2.360233  5  2.0
# 2018-03-04  0.143115  0.363544  1.587648  5  3.0
# 2018-03-05  0.010932  0.802590 -1.701589  5  4.0
# 2018-03-06 -0.354579  0.830066  0.404646  5  5.0

#5. 通过where操作来设置新的值：
df2=df.copy()
df2[df2>0]=-df2
print(df2)
#                    A         B         C  D    F
# 2018-03-01  0.000000  0.000000 -1.385454 -5  NaN
# 2018-03-02 -0.773506 -0.444692 -0.620307 -5 -1.0
# 2018-03-03 -0.506590 -2.445527 -0.664229 -5 -2.0
# 2018-03-04 -0.568711 -0.709224 -2.582502 -5 -3.0
# 2018-03-05 -1.074985 -2.480905 -0.537869 -5 -4.0
# 2018-03-06 -2.659346 -1.055430 -0.379758 -5 -5.0
'''
#四、缺失值处理
# 在pandas中，使用np.nan来代替缺失值，这些值将默认不会包含在计算中，详情请参阅：Missing Data Section。
#1. reindex()方法可以对指定轴上的索引进行改变/增加/删除操作，这将返回原始数据的一个拷贝：
df1=df.reindex(index=dates[0:4],columns=list(df.columns)+['E'])
df1.loc[dates[0]:dates[1],'E']=1
print(df1)
#                    A         B         C         D    E
# 2018-03-01 -0.275255 -0.290044  0.707118  1.094318  1.0
# 2018-03-02 -1.340747  0.633546 -0.911210 -0.275105  1.0
# 2018-03-03 -1.044219  0.659945  1.370910  0.262282  NaN
# 2018-03-04 -0.015582  1.540852 -0.792882 -0.380751  NaN

#2. 去掉包含缺失值的行：
df1=df1.dropna(how='any')
print(df1)
#                    A         B         C         D    E
# 2018-03-01 -0.914568  0.784980 -1.698139 -0.096874  1.0
# 2018-03-02 -0.410249 -0.494166  0.932946 -0.467547  1.0

#3. 对缺失值进行填充：
df1=df1.fillna(value=5)
print(df1)
#                    A         B         C         D    E
# 2018-03-01 -1.265605  0.778767 -0.947968 -1.330982  1.0
# 2018-03-02  1.778973 -1.428542  1.257860  0.362724  1.0
# 2018-03-03 -1.589094 -0.517478 -0.164942 -0.507224  5.0
# 2018-03-04  2.363145  2.089114 -0.081683 -0.184851  5.0