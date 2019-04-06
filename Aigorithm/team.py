'''有 1、2、3、4 个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？'''
def one():
    num_list = [1,2,3,4]
    end = []
    for i in num_list:
        second = []
        second.extend(num_list)
        second.remove(i)
        for j in second:
            third = []
            third.extend(second)
            third.remove(j)
            for k in third:
                end.append(str(i)+str(j)+str(k))
    print(end)
    print("组合数：",len(end))

def two():
    result_list = []
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i != k and j != k and i != j:
                    result_list.append(str(i)+str(j)+str(k))
    print(result_list)
    print("组合数：", len(result_list))
if __name__ == '__main__':
    one()
    two()