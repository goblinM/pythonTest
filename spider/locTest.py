import pandas as pd
#loc可以让你按照索引来进行行列选择。
#iloc就是按照索引的位置来进行选取
#at的使用方法与loc类似，但是比loc有更快的访问数据的速度，而且只能访问单个元素，不能访问多个元素。
def locTest():
    data = [[7,8,9],[0,1,2],[3,4,5]]
    index = ['m','n','p']
    columns = ['a','b','c']
    df = pd.DataFrame(data=data,index=index,columns=columns)
    #法一
    # print(df.ix[1:])
    print(df.ix[1:].iloc[:,[1,2]])
    #法二
    print(df.loc[['n','p'],["b","c"]])
    #法三
    print(df.iloc[1:].iloc[:,[1,2]])
    # print(df.iloc[:[2,3]])
    # print(df.loc(['n','p',['b','c']]))

if __name__ == '__main__':
    locTest()