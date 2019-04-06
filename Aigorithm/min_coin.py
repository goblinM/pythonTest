'''
字节跳动19春招研发第一次在线笔试-A卷的第一道编程题，按照记忆隐约来写的：
小明有1024元的纸币，然后买了一件k元 的物品，然后求找回硬币的最少数量，
然后硬币币值有64,16,4,1一共四种。
比如
输入 k = 200
输出 17
'''
def min_coin(n):
    coin_count = 0
    coin_count += (n // 64)
    other = n % 64
    if other != 0:
        coin_count += (other//16)
        other = other % 16
    if other != 0:
        coin_count += (other // 4)
        other = other % 4
    if other != 0:
        coin_count += (other // 1)
    return coin_count

if __name__ == "__main__":
    total = 1024
    k = 200
    print(min_coin(total-k))