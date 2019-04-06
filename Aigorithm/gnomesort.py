#-*-coding=utf-8-*-
'''
排序算法之：侏儒排序法
从小到大排序
最好情况复杂度O(n)
最坏情况复杂度O(n**2)
'''
def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] < seq[i]:
            i += 1
        else:
            seq[i],seq[i-1] = seq[i-1],seq[i]
            i -= 1
    return seq


seq = [2,5,1,8,3,7,9]
print(gnomesort(seq))
