
class solution:
    """
    冒泡排序：
       1.比较相邻的元素。如果第一个比第二大（升序），就交换两个。
       2.对每个对邻做同样的工作，从开始第一对到结尾的最后一对。
       3.针对所有的元素重复以上步骤，除了最后一个
    例题一：使用冒泡排序将序列3,1,4,1,5,9,2,6,5排序
    """
    def bubble_sort(self,s):
        s_len = len(s)
        for i in range(s_len-1):
            for j in range(i+1,s_len):
                if s[i] > s[j]:
                    s[i],s[j] = s[j],s[i]
        print(s)
        return s

    """
    1、插入排序可以这样看待，是将数据序列分成两部分，前面一部分是有序的，
    后面一部分是无序的。
    2.核心：它把一个无序数列看成两个数列，假如第一个元素构成了第一个数列，
    那么余下的元素构成了第二个数列，很显然，第一个数列是有序的（因为只有
    一个元素嘛，肯定有序哦），那么我们把第二个数列的第一个元素拿出来插
    入到第一个数列，使它依然构成一个有序数列，直到第二个数列中的所有元
    素全部插入到第一个数列，这时候就排好序了。
    例题一：使用插入排序将序列3,1,4,1,5,9,2,6,5排序
    """
    def insert_sort(self,s):
        s_len = len(s)
        for i in range(s_len):
            j = i
            while j > 0:
                if s[j-1] > s[j]:
                    s[j-1],s[j] = s[j],s[j-1]
                j -= 1
            # while 也可以写成这样子
            # for j in range(i):
            #     if s[j-1] > s[j]:
            #         s[j-1], s[j] = s[j], s[j-1]
        return s

    """
    选择排序：选择排序就是每次找出最小的索引，然后替换数据的位置
    选择排序的思路是：
    1、首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    2、再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列
    的末尾。以此类推，直到所有元素均排序完毕。
    """
    def select_sort(self,s):
        # 要的是最小的下标，然后交换
        s_len = len(s)
        for i in range(s_len):
            min_index = i
            for j in range(i+1,s_len):
                if s[min_index] > s[j]:
                    min_index = j
            # 循环一次后找到最小的数字的下标
            s[i],s[min_index] = s[min_index],s[i]
        return s

    """
    希尔排序：希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
    随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分
    成一组，算法便终止
    希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。
    希尔排序是非稳定排序算法。
    增量怎么取？增量因子序列可以有各种取法有取奇数的，也有去质数的
    """

    def shell_sort(self,s):
        step = len(s)//2
        while step > 0:
            for i in range(step,len(s)): #这里要在s[step:len(s)]中进行插入排序
                while i >= step:
                    if s[i-step] > s[i]:
                        s[i-step],s[i] = s[i],s[i-step]  # 这一块类似前段为有序，后半段无序，然后比较
                        i -= step
            step /= 2
        return s

    """
    快速排序：通过一趟排序将要排序的数据分割成独立的两部分，其中
    一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两
    部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据
    变成有序序列
    """
    def quick_sort(self,s):
        if not s:return []
        quick_mid = s[0]  # 这个作为中介值
        # 这个是一个list，list里面的所有值都小于等于quick_mid，然后递归再对其快排
        quick_left = self.quick_sort([i for i in s[1:] if i <= quick_mid])
        # 这个是一个list，list里面的所有值都大于于quick_mid
        quick_right = self.quick_sort([i for i in s[1:] if i > quick_mid])
        return quick_left + [quick_mid] + quick_right

    """
    堆排序：它是选择排序的一种。可以利用数组的特点快速定位指定索引的元素。
    堆分为大根堆和小根堆，是完全二叉树。大根堆的要求是每个节点的值都不大于
    其父节点的值，即A[PARENT[i]] >= A[i]；最小堆要求节点元素都不大于其左右孩子。
    在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，
    最大的值一定在堆顶
    基本思想：
    1.将初始待排序关键字序列(R1,R2....Rn)构建成大顶堆，此堆为初始的无序区
    2.将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,......Rn-1)
    和新的有序区(Rn)
    3.由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,......Rn-1)
    调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2....Rn-2)
    和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成
    """
    # 建立大根堆的算法
    # 列表第一个从0开始，节点下标为i,左孩子则为2*i+1,右孩子下标为2*i+2;
    # 列表第一个从1开始，左孩子为2*i,右孩子为2*i+1
    def buidMaxHeap(self,s,start,end):
        """
        :param s: 排序的列表
        :param start: 父节点下标
        :param end: 结束的下标，当前未被访问交换的最大下标
        :return:
        """
        while True:
            left_child = 2*start + 1 # 左孩子的节点下标
            if left_child > end:
                break
            if left_child + 1 <= end and s[left_child+1] > s[left_child]:
                left_child += 1
            if s[left_child] > s[start] : # 当左右孩子的最大值大于父节点，则交换
                s[left_child],s[start] = s[start],s[left_child]
                # 交换之后以交换子结点为跟的堆不可能是大顶堆，需要重新调整
                start = left_child
            else:
                break
            print(">>>",s)

    # 堆排序实现
    def heap_sort(self,s):
        # 初始化大顶堆
        first = len(s)//2 - 1  # 最后一个有孩子的节点
        for i in range(first,-1,-1): #逆序，就是从有孩子节点的开始往上爬
            self.buidMaxHeap(s,i,len(s)-1)

        #交换堆顶和堆尾
        for bottom in range(len(s)-1,0,-1): # 逆序
            s[bottom],s[0] = s[0],s[bottom]
            self.buidMaxHeap(s,0,bottom-1) # 堆长度减一，（代表当前节点已经访问过），再从上往下调整为大顶堆
        return s






if __name__ == "__main__":
    test_list = [3,1,4,15,5,9,2,6,8]
    obj = solution()
    # bubble_result = obj.bubble_sort(test_list)
    # print(bubble_result)
    # select_result = obj.select_sort(test_list)
    # print(select_result)
    # shell_result = obj.select_sort(test_list)
    # print(shell_result)
    # quick_result = obj.quick_sort(test_list)
    # print(quick_result)
    heap_result = obj.heap_sort(test_list)
    print(heap_result)


