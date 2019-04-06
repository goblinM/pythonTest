'''
created by goblinM
有一个整形数组arr和一个大小为w的窗口从数组的最左边滑到最右边，窗口每次向右边滑一个位置
如果数组长度为n,窗口大小为w,则一共产生n-w+1个窗口的最大值。
复杂度为n(N)
思路：双端队列来实现窗口最大值的更新。
qmax用来存放列表arr中的下标。
1.qmax为空，直接把下标i放进qmax,放入过程结束
2.如果qmax不为空，取出当前qmax队尾存放的下标，假设为j
··1.如果arr[j]>arr[i],直接把下标放进qmax的队尾，放入过程结束
··2.如果arr[j]<=arr[i],把j从qmax弹出，继续qmax的放入规则
假设遍历到arr[i],qmax的弹出规则：
    如果qmax队头的下标等于i-w,说明当前qmax队头的下标已过期，弹出当前队头的下标即可

'''
class MaxArray:
    def max_array(self,s,w):
        if not s or w < 1 or len(s) < w:
            return None
        qmax = []
        # res = len(s) - w +1 #一共会产生的所有值总数
        res = []
        for i in range(len(s)):
            while qmax and s[qmax[-1]] <= s[i]:
                qmax.pop()

            qmax.append(i)
            if qmax[0] == i-w:
                qmax.pop(0)
            if i >= w-1:
                res.append(s[qmax[0]])
        return res

if __name__ == "__main__":
    s = [4,3,5,4,3,3,6,7]
    w = 3
    obj = MaxArray()
    print(obj.max_array(s,w))