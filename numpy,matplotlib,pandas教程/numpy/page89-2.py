import numpy as np
import matplotlib.pyplot as plt
# 从0开始算行和列
uk_file_path = "D:/Study/数据分析课程/DataAnalysis-master (1)/DataAnalysis-master/day03/code/youtube_video_data/GB_video_data_numbers.csv"
us_file_path = "D:/Study/数据分析课程/DataAnalysis-master (1)/DataAnalysis-master/day03/code/youtube_video_data/US_video_data_numbers.csv"

# t1=np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)#unpack相当于T^-1
t_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

t_uk=t_uk[t_uk[:,1]<=500000]

t_uk_comments=t_uk[:,-1]
t_uk_like=t_uk[:,1]



plt.figure(figsize=(20,8),dpi=80)
plt.scatter(t_uk_like,t_uk_comments)

plt.show()