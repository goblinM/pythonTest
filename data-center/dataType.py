'''
    Created by goblinM 2018-10-24
    数据清洗
'''
from abc import abstractmethod


class DataType(object):
    '''
        *setData()功能说明：设置属性信息
        *getData()功能说明：获取属性信息
        *appendData()功能说明：对数组（集合）类型新增追加数据信息
    '''
    @abstractmethod  #抽象方法
    def setData(self,item,key):
        pass

    def getData(self,item,key):
        pass

    def appendData(self,item,key):
        pass


