'''
x = [i for i in list]
[2,5,6,8,9]
将一个 list 映射为另一个 list，每个元素设为变量i
x = [1 for i in range(n)]
[1,1,1,1]
将列表range(n)映射到列表x，每个元素设为常量1
'''
import sys
from datetime import date
from functools import reduce
import random

def test():
    # test_list = [2,5,6,8,9]
    # x = [i for i in test_list]
    # y = [1 for j in range(1,5)]
    # z = [[0 for i in range(5)] for j in range(10)]
    # print(x)
    # print(y)
    # print(z)
    import re

    t = date.today().strftime("%Y-%m-%d %H:%M:%S")

    print(t)
    a = "not 404 found 张三 99 深圳"
    # s = a.split()  # 切割成list
    s = re.sub('\d+|[a-zA-Z]+', "", a)
    print(s.strip())
    A = [1,2,3,4,5]
    B = [2,2,6,8]
    C = [[1,2],[3,4],[5,6]]


    A.extend(B)
    A.sort()
    s = list(sorted(A,reverse=True))
    print(A)
    print(s)
    print(list(filter(lambda x: x % 2 != 0, A)))
    print(int(6/(-132)))
    d = "  heheh  "
    print(d.strip())
    print(d.lstrip())
    print(d.rstrip())
    foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
    foo.sort(key=lambda x: x, reverse=False)
    print(foo)
    foo2 = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
    foo2.sort(key=lambda x:(abs(x)),reverse=False)
    print(foo2)
    foo2.sort(key=lambda x:x<0,reverse=False)
    print(foo2)
    dic = {"name": "zs", "sex": "man", "city": "bj"}
    # s = list(zip(dic.keys(),dic.values()))
    # s.sort(key=lambda x:x[0])
    # new_dict = {x[0]:x[1] for x in s}
    # print(new_dict)
    key_list = list(dic.keys())
    key_list.sort()
    new_dic = {s:dic[s] for s in key_list}

    s = "info:xiaoZhang 33 shandong"
    sp = re.split(r'\W+', s)
    print(sp) # ['info', 'xiaoZhang', '33', 'shandong']
    import re
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
    for email in email_list:
        ret = re.match("[\w]{4,20}@163\.com$", email)
        if ret:
            print("%s 是符合规定的邮件地址，匹配后结果是:%s" % (email, ret.group()))
        else:
            print("%s 不符合要求" % email)

    phone_list = ["12345678912", "14512314526", "14789523147", "13645123174"]
    for p in phone_list:
        ret = re.match(r"1\d{9}[4,7]",p)
        if ret:
            print("wrong")
            # print(ret.group())
        else:
            print(p)
    print(int(1.4)) #1
    # print(int("1.4")) #1
    v = [[1, 3], [20, 6], [8, 10], [15, 18]]
    v.sort(key=lambda x: x[0], reverse=False)
    print(v)
    s_dict = {"a":3,"c":3,"b":1}
    print()
    key_sort = sorted(list(s_dict.values()))
    print(key_sort)
    return list(filter(lambda x: x > 10, list(map(lambda x: x ** 2, A))))

def fn():
    D = [1, 4, 5, 3, 7, 8]
    # 冒泡排序
    for i in range(len(D)):
        for j in range(i,len(D)):
            if D[i] > D[j]:
                D[i],D[j] = D[j] ,D[i]
    print(D)

    # 方法一
    # sort_list = []
    # while len(D)>0:
    #     min_num = min(p)
    #     D.remove(min_num)
    #     sort_list.append(min_num)
    # print(sort_list)
# 递归求和
def fd(n):
    if len(n) > 0:
        num = n.pop()
        res = num+fd(n)
    else:
        res = 0
    return res

counter = 1
def doLotsOfStuff():
    global counter
    for i in (1, 2, 3):
        print(i)
        counter += 1

def fib(s):
    # s = int(sys.stdin.readline().strip())
    # print(s)
    n, a, b = 0, 0, 1
    while n < s:
        a, b = b, a + b
        n = n + 1
    return a



# t = fd([1, 2, 3, 4, 5])
# print(t)
if __name__ == '__main__':
    # print(fib(19))
    # print("12"*8)
    result = 0
    for i in range(100):
        if i % 2 != 0:
            result += i
    print(result)
    print(sum([i for i in range(1,100,2)]))
    s = [random.randint(0, 100) for i in range(20)]
    # 排序
    ls = s[0:20:2]
    ls.sort(reverse=True)
    i = 0
    for j in range(0,20,2):
        s[j] = ls[i]
        i += 1

    x = "i am a teacher,i am man, and i am 38 years old.I am not a businessman."
    x_list = x.split()
    t = x_list.count('i')
    if t == 0:
        print(x)
    else:
        for i in range(len(x_list)):
            if x_list[i] == 'i':
                x_list[i] = 'I'
        print(" ".join(x_list).strip())
    # print(test())
    # # fn()
    # doLotsOfStuff()
    # print(counter)
    # res = []
    # A = [3,4,4,1]
    # for i in A:
    #     if len(res) >= 3:
    #         max_num = max(i, min(res))
    #         if max_num not in res:
    #             res.append(max_num)
    #             res.pop(res.index(min(res)))
    #     else:
    #         res.append(i)
    # result = res[0] * res[1] * res[2]
    # print(result)