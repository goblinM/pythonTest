from functools import reduce
from timeit import timeit

#二叉树
class Tree:
    def __init__(self,left,right):
        self.right = right
        self.left = left

class mulTree:
    def __init__(self,kids,next=None):
        self.kids = self.val = kids
        self.next = next

if __name__ == '__main__':
    t = Tree(Tree("a","b"),Tree("c","f"))
    print(t.right.left)
    mt = mulTree(mulTree("a",mulTree("b",mulTree("c",mulTree("d")))))
    print(reduce(lambda x,y:x+y,range(0,101)))
    print(mt.kids.next.next.val)
    #预测结果 c