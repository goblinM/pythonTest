#python
#@property 把一个getter方法变成属性例如：set_width加上@property变成了属性，@set_width.setter负责把一个setter方法变成属性赋值
#只加@property（即只定义getter方法，不定义setter方法就把该属性变成为只读属性
class Screen(object):
    @property
    def set_width(self):
        return self.width
    @set_width.setter
    def set_width(self,value):
        self.width = value

    @property
    def set_height(self):
        return self.height

    @set_height.setter
    def set_height(self, value):
        self.height = value

    @property  #只读
    def resolution(self):
        return self.width*self.height

s = Screen()
s.width = 1024
s.height = 768
print('resolution = ',s.resolution)
if s.resolution == 786432:
    print("测试通过")
else:
    print("测试失败")