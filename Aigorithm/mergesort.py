#-*-coding=utf-8-*-
'''
排序算法之：归并排序法
这个还有问题
'''
def mergesort(seq):
    mid = len(seq)//2 #取整
    left, right = seq[:mid], seq[:mid]
    if len(left) > 1: left = mergesort(left)  #这里是指分别给左右排序
    if len(right) > 1:right = mergesort(right)
    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res

seq = [12,5,1,56,54,3,8,4,3,95,13,59,20,33]
print(mergesort(seq))