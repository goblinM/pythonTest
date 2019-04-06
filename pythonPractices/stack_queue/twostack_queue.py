'''
created by goblinM 2019-03-26
两个栈组成一个队列
队列：FIFO 先进先出
思路：一个A栈push作为压入栈,另一个B栈为空则把A栈的元素pop弹出栈
'''

class MyQueue:
    def __init__(self):
        self.pushStack = [] #压入栈
        self.popStack = [] #弹出栈

    def push(self,val):
        self.pushStack.append(val)

    def pop(self):
        if self.popStack:
            return self.popStack.pop()
        else:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
            return self.popStack.pop()

    #队列是否为空
    def empty(self):
        return len(self.popStack)==0 and len(self.pushStack)==0

    #获取队列头部元素
    def peek(self):
        if self.popStack:
            return self.popStack[-1]
        else:
            return self.pushStack[0]
if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    print(param_2)
    print(param_3)
    print(param_4)