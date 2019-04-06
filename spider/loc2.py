import pandas as pd
data = [[1,2,3],[4,5,6]]

index = ['d','e']
columns=['a','b','c']

df = pd.DataFrame(data=data,index=index,columns=columns)
# print(df)
#iloc 列数 ix行数
# print(df.iloc[0:])
# print(df.iloc[:,[1]])
print(df.ix[0])
