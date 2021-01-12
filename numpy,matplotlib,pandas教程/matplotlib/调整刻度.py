import matplotlib.pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

#显示中文
# font = {'family': 'Microsoft YaHei',
#         'weight': 'bold',
#         'size': '10'}
# matplotlib.rc('font',**font)
#matplotlib.rc('font',family='Microsoft YaHei',weight='bold')

#my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

plt.rcParams["font.sans-serif"] = ["SimHei"]


x = range(0,120)
y=[random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

#调整x轴的刻度
_xtick_label = ["10点{}分".format(i) for i in range(60)]
_xtick_label += ["11点{}分".format(i) for i in range(60)]
#取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::3],_xtick_label[::3],rotation=90) #rotaion旋转的角度

#添加描述信息
plt.xlabel("时间")
plt.ylabel('温度')
plt.title('表')

plt.show()

