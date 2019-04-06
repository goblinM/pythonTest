"""
两个队列实现栈
将queue1用作进栈出栈，queue2作为一个中转站
入栈时，直接压入queue1中
出栈时，先将queue1中的元素除最后一个元素外依次出队列，并压入队列queue2中，
将留在queue1中的最后一个元素出队列即为出栈元素，最后还要把queue2中的元素再次压入queue1中
"""
from collections import deque

# 一个队列实现栈
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.deque_n = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.deque_n.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.deque_n.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.deque_n[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.deque_n) == 0

#两个队列实现栈
class MyStack2:
    def __init__(self):
        self.queue_one = []
        self.queue_two = []

    def push(self,x):
        self.queue_one.append(x)

    def pop(self):
        one_len = len(self.queue_one)
        for i in range(one_len-1): #剩下最后一个
            self.queue_two.append(self.queue_one.pop(0))
        res = self.queue_one.pop()
        two_len = len(self.queue_two)
        for j in range(two_len):
            self.queue_one.append(self.queue_two.pop(0))
        return res

    def top(self):
        return self.queue_one[-1]

    def empty(self):
        return self.queue_one == []


# obj = MyStack()
obj = MyStack2()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()