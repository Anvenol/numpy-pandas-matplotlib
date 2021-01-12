import numpy as np

#从0开始算行和列
us_file_path="./"
uk_file_path="./"

t1=np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)#unpack相当于T^-1
t2=np.loadtxt(us_file_path,delimiter=",",dtype="int")
t1.transpose()
t1.swapaxes()
t1*T
print(t1)

#取列
print(t2[:,0])
print(t2[:,2:])
print(t2[:[0,2]])

#取行
print(t2[2])
print(t2[2:])
print(t2[[2,8,10]])#取2，8，10行

#取多行多列
print(t2[2,3])#3行4列
print(t2[2:5,1:4])取3-5行，2-4列

#单个
t2[[0,1,2,3,4],[0,1,2,3,4]]

#t2小于10的值变成3
t2[t2<10]=3
