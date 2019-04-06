'''
字节跳动19春招研发第一次在线笔试-A卷的第4道编程题，按照记忆隐约来写的：
第一行，n根初始绳子，m为所需平分的绳子
第二行是指 n根初始绳子每根的初始长度
求最长的平均绳长（保留两位小数）
输入如： 3  4
         3  5 4
输出：2.5

'''
def avg_rope(one,two):
    '''
    :param n: list ,存储n以及m
    :param m: list,存储n根绳子每根的长度
    :return: 最长的平均绳长
    '''
    sum_rope = sum(two) #所有绳子的总长
    n = one[0] # 初始绳子的总数
    m = one[1] # 所需平分的绳子数
    avg_s = float("{:.2f}".format(sum_rope/m))
    print(avg_s)
    count = 0
    while count != m:
        for i in range(n):
            count += (two[i]//float(avg_s))
        if count != m:
            c = max(two)//float(avg_s)
            c = "{:.2f}".format(c)
            #avg_s = avg_s - (float(max(two))-(float(avg_s)*float(c)))/m  这一块的递减有问题
            avg_s -= 0.01
            count = 0
    return avg_s

if __name__ == "__main__":
    list_one = [3,5]
    list_two = [5,5,4]  # 答案应该为2.5
    print(avg_rope(list_one,list_two))