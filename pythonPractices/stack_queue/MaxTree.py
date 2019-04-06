'''
created by goblinM
构造数组的MaxTree
给定一共没有重复的数组arr,写出生出这个数组的MaxTree的函数，要求如果数组长度为N,
则时间复杂度为O(N),额外空间复杂度为O(N)
MaxTree定义如下：
    1.数组必须无重复元素
    2.MaxTree是一棵二叉树，数组的每一个值对应一个二叉树节点
    3.包括MaxTree树在内且在其中的每一棵子树上，值最大的节点都是树的头
思路：
    ·每一个数的父节点是它左边第一个比它大的数和它右边第一个
    比它大的树中，较小的那个。
    ·如果一个数左边没有比它大的数，右边也没有，也就是说，这个数是
    整个数组的最大值，那么这个数是整个数组的最大值，那么这个数是MaxTree的头结点。
接下来的只要知道每一个数左边比它大的数以及右边比它大的数，剩下的工作就很好实现了。如何实现呢？使用栈。
　　
　　从左到右遍历数组arr，假设遍历到的位置为i，如果栈为空或者栈顶元素大于arr[i]，
    直接将arr[i]压入栈中；否则将栈中小于arr[i]的元素全部出栈，然后压入arr[i]。
    同时，栈中元素的左边第一个比它大的数就是它相邻的数，右边第一个比它大的数就
    是使它出栈的数，如果没有数使它出栈，说明它右边没有比它大的数。

　　以[3,1,2]为例，首先3入栈，接下来1比3小，直接入栈，并且确定了1左边第一个比
   它大的数是3；接下来2比1大，1出栈，同时可以确定1右边第一个比它大的数是2；
   接下来2比3小，2入栈，并且确定了2左边第一个比它大的数是3。
   此时栈中的元素为[3,2]，没有数使它们出栈，所以3和2右边都没有比它大的数。

'''
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class MaxTree:
    def getMaxTree(self,s):
        arr = [TreeNode(i) for i in s] #构造每一个可能的节点
        leftTree = {} #左子树
        rightTree = {} #右子树
        stack = []
        for i in range(len(arr)):
            curNode = arr[i] #当前的节点
            while stack and stack[-1].val < curNode.val:
                cur = stack.pop() #出栈
                leftTree[cur] = stack[-1] if stack else None
                rightTree[cur] = curNode
            stack.append(curNode)

        while stack:
            cur = stack.pop()
            leftTree[cur] = stack[-1] if stack else None
            rightTree[cur] = None

        head = None
        for i in range(len(arr)):
            curNode = arr[i]
            left = leftTree[curNode]
            right = rightTree[curNode]
            if left == None and right == None:
                head = curNode
            elif left == None:
                if right.left == None:
                    right.left = curNode
                else:
                    right.right = curNode
            elif right == None:
                if left.left == None:
                    left.left = curNode
                else:
                    left.right = curNode
            else:
                parent = left if left.val < right.val else right
                if parent.left == None:
                    parent.left = curNode
                else:
                    parent.right = curNode
        return head
