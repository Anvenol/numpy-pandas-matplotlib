import pandas as pd
import numpy as np
t3=pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
print(t3)

print(t3.loc["a","Z"])
print(t3.loc["a",:])
print(t3.loc[:,"Z"])
print(t3.loc[["a","c"],["W","Z"]])
print(t3.loc[["a":"c"],["W","Z"]])#冒号在loc里面是左闭右闭