import math
import random
from const import const
import copy
from itertools import product
from const import manhattan_distant


# 棋盘类

class Board:
    # 属性
    food = [4, 5]  # 食物的位置
    head = [0, 0]  # 头部的位置
    tail_Arr = []  # 写入蛇尾的位置

    # 构造函数
    def __init__(self):
        # 清空棋盘 所有的点都设置为无限远
        # for i in range(const.BOARD_HEIGHT):
        #	for j in range(const.BOARD_WIDTH):
        #		self.board[i][j] = const.UNDEFINED
        self.board = [[const.UNDEFINED for i in range(const.BOARD_WIDTH)] for j in range(const.BOARD_HEIGHT)]

    # 方法
    # 根据位置获取对应的值
    def get_value(self, pos):
        return self.board[pos[1]][pos[0]]

    # 根据位置写入对应的值
    def set_value(self, pos, value):
        self.board[pos[1]][pos[0]] = value

    # 打印棋盘的方法
    def board_print(self):
        for i in range(const.BOARD_HEIGHT):
            for j in range(const.BOARD_WIDTH):
                value = str(self.board[i][j])  # str整数转字符串
                if self.board[i][j] == const.FOOD:
                    value = "F"
                elif self.board[i][j] == const.SNAKE_HEAD:
                    value = "H"
                elif self.board[i][j] == const.SNAKE_TAIL:
                    value = "T"
                print(value, end=' ')  # 空格
                if self.board[i][j] < 10:
                    print(end=' ')  # 空格

            print()  # 换行
        print()  # 换行

    # 写入食物的位置
    def set_food(self, food):
        self.food = food

    # 写入蛇头的位置
    def set_head(self, head):
        self.head = head

    # 写入蛇尾的位置,不断append??
    def set_tailArr(self, tailArr):
        self.tail_Arr = tailArr

    # 随机生成食物(即随机生成坐标)
    def initFoodPos(self):
        while True:
            x = math.floor(random.random() * const.BOARD_WIDTH)
            y = math.floor(random.random() * const.BOARD_HEIGHT)
            if [x, y] == self.head:  # 即吃掉食物后继续爬
                continue

            if [x, y] in self.tail_Arr:
                continue

            return [x, y]

    # 坐标按照方向找下一个位置
    # pos描述一个坐标 元组 两个元素x和y
    # direction 方向 left up right down其中一个
    # copy：浅拷贝。只拷贝父对象，不会拷贝对象的内部的子对象,只要改变其他也会跟着变
    # deepcopy：深拷贝。拷贝对象及其子对象这个不会，因为它和初始的是不同的对象

    def move(self, pos, direction):
        nextPos = copy.deepcopy(pos)
        if direction == "left":
            nextPos[0] -= 1
        elif direction == "right":
            nextPos[0] += 1
        elif direction == "up":
            nextPos[1] -= 1
        elif direction == "down":
            nextPos[1] += 1

        return nextPos
    # 蛇头根据方向移动一格
    # 返回移动后的状态
    def move_with_tail(self, direction):
        if not self.move_possible(self.head, direction):
            return const.STATE_GAMEOVER
        food_eated = False
        # 蛇头的位置添加到蛇尾(即吃完的食物也就蛇头的位置作为蛇尾不断插入，然后蛇头往前移动一格）
        self.tail_Arr.insert(0, self.head)
        # 蛇头移动一格
        self.head = self.move(self.head, direction)
        # 判断蛇头是否碰到食物
        if self.head == self.food:
            # 吃到食物，此刻从新生成食物
            self.food = self.initFoodPos()
            food_eated = True
        else:
            # 当蛇头没碰到食物继续移动，蛇尾也跟着变，把之前的坐标pop出来
            self.tail_Arr.pop()
        if food_eated:
            return const.STATE_EAT_FOOD
        else:
            return const.STATE_MOVE

    # 假设蛇头是在pos位置上 判断往direction方向移动的时候 是否越界
    # 如果越界返回False 越界返回True
    def is_in_board(self, pos, direction):
        nextPost = self.move(pos, direction)
        # 判断
        if nextPost[0] < 0 or nextPost[0] > const.BOARD_WIDTH or nextPost[1] < 0 or nextPost[1] > const.BOARD_HEIGHT:
            return False
        else:
            return True

    # 假设蛇头是在pos位置上 检测是否可以往direction方向移动
    def move_possible(self, pos, direction):
        if not self.is_in_board(pos, direction):
            return False
        # 判断蛇头与蛇尾是否相撞
        nextPos = self.move(pos, direction)
        if nextPos in self.tail_Arr:
            return False
        else:
            return True

    # 重置棋盘的方法
    def board_reset(self):
        for i, j in product(range(const.BOARD_WIDTH), range(const.BOARD_HEIGHT)):
            # 食物
            if [i, j] == self.food:
                self.board[j][i] = const.FOOD
            # 蛇头
            elif [i, j] == self.head:
                self.board[j][i] = const.SNAKE_HEAD
            # 蛇尾
            elif [i, j] in self.tail_Arr:
                self.board[j][i] = const.SNAKE_TAIL
            # 其他
            else:
                self.board[j][i] = const.UNDEFINED

    # 从食物位置出发 广度优先搜索遍历整个棋盘
    # 计算出board中每个非蛇头蛇尾的点到达食物的距离
    def board_refresh(self):
        # self.board_print()
        # 把遍历过的点保存起来 压到queue栈 while循环 每次从queue栈中取一个值 直到栈为空为止
        queue = []
        # 把食物的点压到栈中
        queue.append(self.food)
        # 用于记录该点是否被访问过的列表 未访问过的点置为0 访问过则置1
        # [0 for i in range(const.BOARD_WIDTH)] ==>> [[0,0,0,0,0,0,0,.....,0] for j in range(const.BOARD_HEIGHT)] ==> [[0,0,0,0,..0],[0,0,0,0,..0],[0,0,0,0,..0],...,[0,0,0,0,..0]]
        inqueue = [[0 for i in range(const.BOARD_WIDTH)] for j in range(const.BOARD_HEIGHT)]
        # 标记是否能找到蛇头
        found = False
        # 开始循环
        while True:
            # 如果queue中已经没有可以遍历的点 则退出循环
            if len(queue) == 0:
                break
            # 从queue中取出一个点
            idx = queue.pop(0)
            # 如果这个点已经访问过 则忽略
            if inqueue[idx[1]][idx[0]] == 1:
                continue
            # 开始遍历这个点 把这个点设置为已经访问过
            inqueue[idx[1]][idx[0]] = 1
            # 遍历4个方向
            dir = ["left", "up", "right", "down"]
            for i in range(4):
                # 判断是否可以往这个方向移动 去寻找食物
                if self.move_possible(idx, dir[i]):
                    # 如果可以移动 则对移动后的点进行判断
                    next = self.move(idx, dir[i])
                    #判断棋盘位置
                    if self.is_in_board(next,dir[i]):
                        # 如果移动后的点是蛇尾 则循环结束
                        if next == self.head:
                            found = True
                        # 如果移动后的点不是蛇尾 可以把该点记录下来
                        elif next not in self.tail_Arr:
                            # 如果这点现在计算出来的距离比原来的距离要小 则可以把计算出来的值写入
                            if self.get_value(next) > self.get_value(idx) + 1:
                                # 注意食物周边的点需要标记为1 其他点标记为参考点+1
                                if self.get_value(idx) == const.FOOD:
                                    self.set_value(next, 1)
                                else:
                                    self.set_value(next, self.get_value(idx) + 1)
                            # 如果这点没有在inqueue中被标记 则是没有被访问过 则需要把该点添加到queue列表中
                            if inqueue[next[1]][next[0]] == 0:
                                queue.append(next)

        return found

        # 判断两点之间是否有障碍
        # 返回False表示无障碍 返回True表示有障碍

        # 判断两点之间是否有障碍
        # 返回False表示无障碍 返回True表示有障碍
    def is_obstacle_between(self, startPos, endPos):
        if startPos == endPos:
            return False
        # 如果移动后有障碍，说明不能往该方向移动 仅此而已 但还可能可以往其他方向移动
        # 如果移动后无障碍，就真的无障碍了
        dir = ["left", "up", "right", "down"]
        for i in range(4):
            # 判断是否可以往这个方向移动 去寻找目标
            if self.move_possible(startPos, dir[i]):
                # 移动后的点
                next = self.move(startPos, dir[i])
                # 如果移动后的点与目标点的距离增加 则该方向直接忽略
                if manhattan_distant(next, endPos) > manhattan_distant(startPos, endPos):
                    continue
                # 对移动后的点进行判断
                if next == endPos:
                    # 如果移动后的下一个点就是目标点 则显然无障碍
                    return False
                else:
                    # 否则 对移动后的点与目标点之间的障碍进一步 递归
                    ret = self.is_obstacle_between(next, endPos)
                    if not ret:
                        return False
        # 只有尝试了所有的方向后 才返回True
        return True

    #蛇尾当做食物 障碍返回True 无障碍返回False
    def is_tail_inside(self, startPos, endPos):
        self.board_refresh()
        self.board_reset()
        #当蛇头与蛇尾相碰
        if startPos == endPos:
            print("true1")
            return True
        dir = ["left", "up", "right", "down"]
        for i in range(4):
            # 判断是否可以往这个方向移动 去寻找目标
            if self.move_possible(startPos, dir[i]):
                # 移动后的点
                next = self.move(startPos, dir[i])
                if manhattan_distant(next, endPos) < manhattan_distant(startPos, endPos):
                    continue
                # 对移动后的点进行判断
                if next == endPos:
                    print("true2")
                    # 如果蛇头与蛇尾紧挨着则返回TRUE，即不能继续运动了
                    return True
                else:
                    # 否则 对移动后的点与目标点之间的障碍进一步 递归
                    ret = self.is_tail_inside(next, endPos)
                    if not ret:
                        print('222222222222')
                        return False
        # 只有尝试了所有的方向后 才返回True
        return True

