'''
栈:先进后出 FILO
设计一个有最小功能的栈
1.时间复杂度为o(1)
'''

class solution:

    def __init__(self):
        self.min_res = None #这个存储最小数值
        self.stack = [] #这个存储栈

    # 插入
    def push(self,val):
        if self.min_res is None:
            self.min_res = val
        else:
            self.min_res = min(self.min_res,val)
        self.stack.append(val)

    # 弹出
    def pop(self):
        if self.stack:
            t = self.stack.pop()
            if self.min_res == t:
                self.min_res = min(self.stack)
            return t
        else:
            raise  Exception("Stack is Empty")


    def getMin(self):
        if self.stack:
            return self.min_res
        else:
            raise Exception("Stack is Empty")

if __name__ == "__main__":
    obj = solution()
    obj.push(1)
    obj.push(3)
    print(obj.pop())
    obj.push(6)
    obj.push(2)
    obj.push(5)
    print(obj.getMin())