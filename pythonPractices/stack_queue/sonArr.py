'''
created by goblinM
最大值减去最小值小于或等于num的子数组数量
给定数组arr和整数num,共返回有多少个子数组满足如下情况：
    ·max(arr[i...j])-min(arr[i...j])<= num
    ·max(arr[i...j])表示数组arr[i...j]中的最大值，
    min(arr[i...j])表示子数组arr[i...j]中的最小值
如果数组长度为N，请实现时间复杂度为o(N)的解法
思路：双端队列：qmax和qmin.当子数组为arr[i..j]时，qmax维护了窗口子数组arr[i..j]
的最大值更新的结构。qmin维护了窗口子数组arr[i..j]的最小值更新的结构。当子数组arr[i..j]
向右扩一个位置变成arr[i..j+1]时，qmax和qmin结构可以在o(1)的时间内更新，并且可以在o(1)
的时间内得到arr[i..j+1]的最大值和最小值。当子数组arr[i..j]向左缩一个位置变成arr[i+1..j]
时，qmax和qmin结构依然可以在0(1)的时间内更新，并且在o(1)的时间内得到arr[i+1..j]的最大值和最小值
'''
class sonArr:
    def getNum(self,num,arr):
        if arr == None or len(arr) == 0:
            return 0
        qmin = []
        qmax = []
        i,j=0,0
        res = 0
        while i < len(arr):
            while j < len(arr):
                while qmin and arr[qmin[-1]] >= arr[j]:
                    qmin.pop()
                qmin.append(j)
                while qmax and arr[qmax[-1]] <= arr[j]:
                    qmax.pop()
                qmax.append(j)
                if arr[qmax[0]] - arr[qmin[0]] > num:
                    break
                j += 1
            if qmin[0] == i:
                qmin.pop(0)
            if qmax[0] == i:
                qmax.pop(0)
            res += j - i
            i += 1
        return res