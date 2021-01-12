import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path="D:/Study/数据分析课程/DataAnalysis-master (1)/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

#rating,runtime分布情况
#选择图形，直方图
#准备数据
runtime_data = df["Runtime (Minutes)"].values

max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

#计算组数
print(max_runtime-min_runtime)
num_bin = (max_runtime - min_runtime) // 0.5

# 设置图形的大小
plt.figure(figsize=(20, 8), dpi=80)
plt.hist(runtime_data, num_bin)

_x = [min_runtime]
i = min_runtime
while i <= max_runtime + 0.5:
    i = i + 0.5
    _x.append(i)

plt.xticks(_x)

plt.show()

