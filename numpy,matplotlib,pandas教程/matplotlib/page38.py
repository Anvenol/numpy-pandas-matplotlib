from matplotlib import pyplot as plt


plt.rcParams["font.sans-serif"] = ["SimHei"]

y3=[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y10=[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x3=range(1,32)
x10=range(51,82)

plt.figure(figsize=(20,8),dpi=90)

#绘制散点图
plt.scatter(x3,y3,label="3")
plt.scatter(x10,y10,label='10')
plt.legend(loc="upper left")

#调整x的刻度
_x=list(x3)+list(x10)
_xtick_label=["3月{}日".format(i) for i in x3]
_xtick_label +=["10月{}日".format(i) for i in x10]
plt.xticks(_x,_xtick_label,rotation=45)

#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("标题")
plt.show()