'''
created by goblinM
如何仅用递归函数和栈操作逆序一个栈
思路：其功能是返回并移除栈底元素。之后再实现一个递归函数 b，
其功能是不断用递归的临时变量去接住 a 函数返回的栈底元素，
这样，最后一个栈底元素就是原来栈的栈顶元素，之后一层一层的将
递归中的临时变量压入栈中，这样就实现了逆序
'''
class reverseStack:
    #递归函数一：将栈stack的栈底元素返回并移除
    def reverse_stack_list(self,s):
        res = s.pop()
        if not s:
            return res
        else:
            last = self.reverse_stack_list(s)
            s.append(res)
            return last

    #递归函数二：逆序一个栈，实现题目
    def reverse_act(self,s):
        if not s:
            return
        i = self.reverse_stack_list(s)
        self.reverse_act(s)
        s.append(i)
        return s

obj = reverseStack()
s = [1,2,3,4,5]
print(obj.reverse_act(s))