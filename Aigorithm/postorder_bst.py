#输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
#思路(错误)：先把数组构造成一棵二叉搜索树，然后再后序遍历，看处理得到的数组和开始的数组是否一致
#思路别人的启发：对于一个序列S，最后一个元素是x （也就是根），如果去掉最后一个元素的序列为T，
# 那么T满足：T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。完美的递归定义 。
class solution:
    # 这个函数用来比较
    def VerifyOfBST(self,s):
        if len(s) == 0:
            return False
        return self.IsBST(s,0,len(s)-1)

    def IsBST(self,s,start,end):#,start,end
        '''
        :param s:需要比较的数组
        :param start: 开始的下标
        :param end: 结束的下标
        :return:
        '''
        if start >= end:
            return True
        root = end # 根节点的下标后序遍历，最后一个为跟结点
        # 找出左右子树的切割序列
        while root > start and s[root-1] > s[end]:
            root -= 1
        for j in range(start,root):
            if s[j] > s[end]:
                return False
        # print(s[-1])
        # left_list = [i for i in s[:-2] if i < s[-1]]
        # right_list = [i for i in s[:-2] if i > s[-1]]
        # #左子树的元素都需要小于根节点
        # for i in left_list:
        #     if i > s[-1]:
        #         return False
        #
        # for j in right_list:
        #     if j < s[-1]:
        #         return False
        #递归判断左子树与右子树是否满足后序遍历
        return self.IsBST(s,start,root-1) and self.IsBST(s,root,end-1)

    # 这个函数是用来二叉搜索树的插入
    def BST_Insert(self,s):
        pass

    # 这个函数是构造二叉搜索树的
    def BST_Create(self,s):
        pass

    # 这个是后序遍历的
    def Post_Order(self,s):
        pass

class Solution:
    def VerifySquenceOfBST(self,sequence):
        # write code here
        if len(sequence)==0:
            return False
        index = 0
        for i in range(len(sequence)):
            if sequence[i]>sequence[-1]:
                index = i
                break
        for j in range(i,len(sequence)):
            if sequence[j]<sequence[-1]:
                return False
        left = True
        right = True
        if len(sequence[:index])>0:
            left = self.VerifySquenceOfBST(sequence[:index])
        if len(sequence[index:-1])>0:
            right = self.VerifySquenceOfBST(sequence[index:-1])
        return left and right


if __name__ == "__main__":
    obj = solution()
    # s = [5,7,6,9,11,10,8]
    s = [7,4,6,5]
    print(obj.VerifyOfBST(s))