'''
created by goblinM
用一个栈B实现另一个栈A的排序
从栈顶到栈底实现从大到小排序
A栈弹出元素为cur
若cur<= B栈的栈顶元素，直接压入
若cur> B栈的栈顶元素,则把B栈元素弹出压入A栈，直到cur 小于或等于B
栈的栈顶元素，再把cur压入B栈
'''
class SortStack:
    def stackdemo(self,s):
        stack_a = []

        while s:
            res = s.pop()
            if not stack_a:
                stack_a.append(res)
            else:
                if res <= stack_a[-1]:
                    stack_a.append(res)
                else:
                    while stack_a:
                        n = stack_a[-1]
                        if res > n:
                            s.append(stack_a.pop())
                        else:
                            stack_a.append(res)
                            break
                    stack_a.append(res)
        while stack_a:
            s.append(stack_a.pop())
        return s

obj = SortStack()
s = [5,4,1,2,3]
print(obj.stackdemo(s))
