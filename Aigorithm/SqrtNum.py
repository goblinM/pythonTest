import math


def SqrtNum():
    for num in range(100000):
        x = int(math.sqrt(num + 100))
        y = int(math.sqrt(num + 268))
        if x*x == num+100 and y*y == num+268:
            print(num)
        # if isinstance(int(math.sqrt(num + 100)),int) and isinstance(int(math.sqrt(num + 268)),int):
        #     print(num)
    # print(isinstance(math.sqrt(4), int))
    # print(math.sqrt(4))
if __name__ == '__main__':
    SqrtNum()