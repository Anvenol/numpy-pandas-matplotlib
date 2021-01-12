import pandas as pd

#pandas 读取csv中的文件
df= pd.read_csv(" ")

print(df[(df["Count"]>800) & (df["Count"]<1000)])



