from matplotlib import pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

x14=list(range(len(a)))
x15=[i+0.2 for i in x14]
x16=[i+0.4 for i in x14]

plt.figure(figsize=(20,8),dpi=80)

plt.bar(range(len(a)),b_14,width=0.2,label="14")
plt.bar(x15,b_15,width=0.2,label="15")
plt.bar(x16,b_16,width=0.2,label="16")
plt.legend()

plt.xticks(x15,a)

plt.show()