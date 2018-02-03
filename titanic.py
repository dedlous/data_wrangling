import numpy as np
import pandas as pd
import sys
f_handler=open('out.log', 'w')
sys.stdout=f_handler
titanic_file_name='titanic-data.csv'
df=pd.read_csv(titanic_file_name,index_col='PassengerId')
print (df[:5])
print (df[df['Age']>60])
# print (df._ix)




# def loadCSVfile2():
#
#     tmp = np.genfromtxt(titanic_file_name, dtype=np.str, delimiter=",")
#     data = tmp[1:,1:].astype(np.float)#加载数据部分
#     label = tmp[1:,0].astype(np.float)#加载类别标签部分
#     return data, label #返回array类型的数据
#
# data,label=loadCSVfile2()
# print (label)