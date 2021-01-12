import pandas as pd
from pymongo import MongoClient

client=MongoClient()
collection= client["douban"]["tv1"]
data =list(collection.find())

df=pd.DataFrame(data)