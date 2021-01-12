import pandas as pd
import numpy as np
file_path="D:/Study/数据分析课程/DataAnalysis-master (1)/DataAnalysis-master/day05/code/IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)
#print(df.info())
print(df.head(1))

#获取平均分
print(df["Rating"].mean())

#导演的人数
#print(len(set(df["Director"].tolist())))
print(len(df["Director"].unique()))

#获取演员的人数
temp_actor_list = df["Actors"].str.split(", ").tolist()
actor_list = [i for j in temp_actor_list for i in j]
actor_num= len(set(actor_list))
print(actor_num)