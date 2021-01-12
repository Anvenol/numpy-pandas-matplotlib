import numpy as np

np.where(t<10,0,10)#t<0的等于0，否则等于10
t.clip(10,18)#小于10的都等于10，大于18的都等于18

#计算nan的个数
np.count_nonzero(t2!=t2)
np.count_nonzero(np.isnan(t2))
#判断是否为nan
np.isnan(t2)

t3=np.arange(12).reshape(3,4)
print(t3)

print(np.sum(t3))
print(np.sum(t3,axis=0))#列的值
print(np.sum(t3,axis=1))#行的值
