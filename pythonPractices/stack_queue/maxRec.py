'''
created by goblinM
求最大子矩阵的大小
给定一个整形矩阵map，其中的值只有0和1两种，求其中全
是1的所有矩形区域中，最大的矩形区域为1的数量
如果矩阵的大小是O(N*M)，本题可以做到时间复杂度为O(N*M)。
1、矩阵的行数是N，以每一行做切割，统计以当前行作为底的情况下，每个位置往上连续1的数量。使用高度数组height来表示。
　　例如：
　　map = 1　0　1　1
　　　 　　1　1　1　1
　　　　 　1　1　1　0
　　以第一行做切割后，height = {1, 0, 1, 1}.
　　以第二行做切割后，height = {2, 1, 2, 2}.
　　以第三行做切割后，height = {3, 2, 3, 0}.

2、对于height数组，我们可以将其想象成一个直方图，要求最大的子矩阵，实际上就是对以每一行为底的直方图，其最大矩阵面积。如果我们能求出以每一个柱子扩展出去的最大矩形，那么其中最大的矩形就是我们想要的。

　　如果要求一个柱子a扩展出去的最大矩形，实际上就是求这个柱子左边第一个比它低的柱子b以及右边第一个比它低的柱子c，
    那么b和c之间的柱子数×a柱子的高度，就是答案。问题的关键就在于如何快速的找到柱子b和c。方法如下：
　　
　　使用一个栈，从左到右遍历数组height，假设遍历到的位置为i，如果栈为空或者栈顶所对应的元素小于height[i]，直接将 i 压入栈中；否则将栈中大于height[i]的元素全部出栈，然后压入 i。对于栈中的每一个元素，左边第一个比它小的数的位置就是栈中上一个元素，右边第一个比它小（或者等于）的数的位置就是使它出栈的数的位置，如果没有数使它出栈，说明它右边没有比它小的数。

　　以[1,3,2]为例，首先1入栈，接下来3比1大，直接入栈，并且确定了3左边第一个比它小的数是1；接下来2比3小，3出栈，同时可以确定3右边第一个比它小的数是2；接下来2比1大，2入栈，并且确定了2左边第一个比它小的数是1。此时栈中的元素为[1,2]，没有数使它们出栈，所以1和2右边都没有比它小的数。
'''
class maxRecSize:
    def maxRecFromBottom(self,height):
        if height == None or len(height) == 0:
            return 0
        stack = []
        maxArea = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] >= height[i]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                maxArea = max(maxArea,(i-k-1)*height[i])
            stack.append(i)

        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            maxArea = max(maxArea,(len(height)-k-1)*height[j])
        return maxArea
    
    def maxRecArea(self,map):
        # map为二维数组
        if map == None or len(map) == 0 or len(map[0]) == 0:
            return 0
        height = [0 for i in range(len(map[0]))]
        maxArea = 0
        for i in range(len(map)):
            for j in range(len(map[0])):
                height[j] = 0 if map[i][j] == 0 else height[j] + 1
            maxArea = max(maxArea,self.maxRecFromBottom(height))

        return maxArea