"""
两个list实现，A栈作为压栈push,B栈作为弹出栈pop;
push的时候，把结果压入A栈，并且判断B栈是否为空，如果为空，A中所有的元素移动到B栈。
pop的时候，判断A,B栈是否为空，如果同时为空，抛出异常，如果不同时为空，判断B栈是否有元素，
如果没有，则将A栈中元素全部移动到B栈中，进行弹出。
"""
#两个栈实现队列
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        栈先进后出
        """
        self.stack_one = []  # 压入栈
        self.stack_two = []  # 弹出栈

    def push(self, x: 'int') -> 'None':
        """
        Push element x to the back of queue.
        """

        self.stack_one.append(x)

    def pop(self) -> 'int':
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_two:  # 弹出栈为空的时候把压入栈的所有元素放至弹出栈中
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())
        return self.stack_two.pop()

    def peek(self) -> 'int':
        """
        Get the front element.
        """

        if self.stack_two:
            return self.stack_two[-1]
        else:
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())
        return self.stack_two[-1]

    def empty(self) -> 'bool':
        """
        Returns whether the queue is empty.
        """
        if len(self.stack_one) == 0 and len(self.stack_two) == 0:
            return True
        return False

#一个栈实现队列
class MyQueue2:
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        '''
        获取队头元素
        :return:
        '''
        return self.stack.pop(0)
    def peek(self):
        '''
        获取顶端的数字
        :return:
        '''
        return self.stack[0]
    def empty(self):
        return self.stack == []
# queue = MyQueue()
queue = MyQueue2()
queue.push(1)
queue.push(2)
queue.peek()  # 返回 1
queue.pop()   # 返回 1
queue.empty() # 返回 false