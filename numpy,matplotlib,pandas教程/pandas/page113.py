import pandas as pd
df= pd.read_csv("")

#排序
df=df.sort_values(by="Count_AnimalName")#ascending=False ,变成降序
print(df.tail((10)))

#数组表示取行，字符串表示取列
#取前20行
print(df[:20])
#取一列
print(df["Row_Labels"])



