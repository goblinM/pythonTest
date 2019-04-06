"""
# __init__,__new__的区别
"""
# class Test:
#     def __init__(self):
#         print("init的方法：",self)
#         print(id(self))
#
#     def __new__(cls, *args, **kwargs):
#         print("new的id：",id(cls))
#         print("new的方法：",super(Test,cls).__new__(cls))
#         return super(Test,cls).__new__(cls)
#
#
# if __name__ == '__main__':
#     print("init的id",id(Test()))

class Singleton:
    instance = None  # 初始化实例为NULL

    def __new__(cls, xx, yy):

        if cls.instance is None:  # 如果实例为空则实例化
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, xx, yy):
        self.xx = xx
        self.yy = yy

if __name__ == "__main__":
    obj1 = Singleton(1, 2)
    obj2 = Singleton(2, 1) # 最后赋值xx为2，因为单例实例出来的对象是全局通用唯一的，所以xx=2
    print(obj1.xx,obj2.xx)
    print(obj1 is obj2)
    # print(obj1.xx)
