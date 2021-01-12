import numpy as np
import matplotlib.pyplot as plt
# 从0开始算行和列
uk_file_path = "D:/Study/数据分析课程/DataAnalysis-master (1)/DataAnalysis-master/day03/code/youtube_video_data/GB_video_data_numbers.csv"
us_file_path = "D:/Study/数据分析课程/DataAnalysis-master (1)/DataAnalysis-master/day03/code/youtube_video_data/US_video_data_numbers.csv"

uk_data = np.loadtxt(uk_file_path, delimiter=",", dtype="int")
us_data = np.loadtxt(us_file_path, delimiter=",", dtype="int")

#添加国家信息
#构造全为0的数据
zero_data= np.zeros((us_data.shape[0],1)).astype(int)
ones_data= np.ones((uk_data.shape[0],1)).astype(int)

#分别添加一列全为0，1的数组
us_data = np.hstack((us_data,zero_data))
uk_data = np.hstack((uk_data,ones_data))

#拼接两组数据
final_data=np.vstack((uk_data,us_data))
print(final_data)

print(np.eye(3))

np.argmax(t,axis=0)
np.argmin(t,axis=0)