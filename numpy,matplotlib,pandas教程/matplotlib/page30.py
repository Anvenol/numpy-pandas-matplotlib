from matplotlib import pyplot as plt
from matplotlib import font_manager

y1=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2=[1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]

x=range(11,31)

plt.rcParams["font.sans-serif"] = ["SimHei"]
#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y1,label="自己",color="b",linestyle=":")#linewidth
plt.plot(x,y2,label="同桌",color="r",linestyle="-.")

plt.legend(loc="upper left")#loc换legend位置

#x轴刻度
_xtick_label = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_label)

plt.yticks(range(0,8))

#绘制网格
plt.grid(alpha=0.8,linestyle=":")#alpha：透明度设置

#展示
plt.show()