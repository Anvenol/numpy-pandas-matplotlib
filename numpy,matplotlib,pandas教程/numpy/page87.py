import numpy as np

t1=np.arange(12).reshape(3,4).astype(float)

t1[1,2:]=np.nan

def fill_ndarray(t1):
    for i in range(t1.shape[1]):#t1.shape=(3,4)
        temp_col=t1[:,i]
        nan_num=np.count_nonzero(temp_col != temp_col)
        if nan_num!=0:
            temp_not_nan_col = temp_col[temp_col==temp_col]#当前一列不是nan的array
            mean=temp_not_nan_col.mean()
            temp_col[np.isnan(temp_col)]=mean
    return t1

if __name__=="__main__":
    t1=np.arange(24).reshape(4,6).astype(float)
    t1[1,2:]=np.nan
    print(t1)
    t1=fill_ndarray(t1)
    print(t1)

