import numpy as np
import matplotlib.pyplot as plt
# 从0开始算行和列
uk_file_path = "D:/Study/数据分析课程/DataAnalysis-master (1)/DataAnalysis-master/day03/code/youtube_video_data/GB_video_data_numbers.csv"
us_file_path = "D:/Study/数据分析课程/DataAnalysis-master (1)/DataAnalysis-master/day03/code/youtube_video_data/US_video_data_numbers.csv"

# t1=np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)#unpack相当于T^-1
t_us = np.loadtxt(us_file_path, delimiter=",", dtype="int")

t_us_comments=t_us[:,-1]

#选择比5000小的数据
t_us_comments=t_us_comments[t_us_comments<=5000]

print(t_us_comments.max(),t_us_comments.min())

d=50
num_bins=(t_us_comments.max()-t_us_comments.min())//d

plt.figure(figsize=(20,8),dpi=80)
plt.hist(t_us_comments,num_bins)


plt.show()