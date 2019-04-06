from board import *
from const import *
import random
#AI算法类
from const import manhattan_distant


class Algorithm:
    #构造初始函数
    def __init__(self,board):
        self.board = board
    #根据食物位置 蛇头位置 蛇尾位置 来决定下一步移动的方向
    def findDirection(self):

        best_move = self.choose_shortest_safe_move()
        if best_move == "none":
            print('哈哈哈')
            best_move = self.choose_longest_safe_move()
        elif best_move == "nothing":
            print('enenen')
            best_move = self.any_possible_move()
        return best_move

        # 随便找一个可行的方向走
    def any_possible_move(self):
        best_move = "end"
        self.board.board_reset()
        self.board.board_refresh()
        # 在上下左右4个方向中找一个可行的方向去走
        dir = ["left", "up", "right", "down"]
        random.shuffle(dir)  # 洗牌
        for i in range(4):
            if self.board.move_possible(self.board.head, dir[i]):
                best_move = dir[i]
                break

        return best_move

    # 选择最短路径
    def choose_shortest_safe_move(self):
        best_move = "none"
        self.board.board_reset()
        self.board.board_refresh()
        dir = ["left", "up", "right", "down"]
        random.shuffle(dir)  # 洗牌
        for i in range(4):
            # 判断这个方向是否可以移动
            if self.board.move_possible(self.board.head, dir[i]):
                # 移动后的点
                next = self.board.move(self.board.head, dir[i])
                # 判断移动后的点与食物之间的距离是否变短
                if manhattan_distant(next, self.board.food) < manhattan_distant(self.board.head, self.board.food):
                    # 判断移动后与食物之间是否有障碍
                    if not self.board.is_obstacle_between(next, self.board.food):
                        best_move = dir[i]
                        break

        return best_move

    # 选择最长路径
    def choose_longest_safe_move(self):
        best_move = "nothing"
        self.board.board_reset()
        self.board.board_refresh()
        dir = ["left","up","right","down"]
        random.shuffle(dir)
        for i in range(4):
            if self.board.move_possible(self.board.head,dir[i]):
                next = self.board.move(self.board.head,dir[i])
                if self.board.is_in_board(next,dir[i]):
                    #食物的最远距离
                    if manhattan_distant(next, self.board.food) > manhattan_distant(self.board.head, self.board.food):
                        if not self.board.is_tail_inside(next,self.board.food,self.board.tail_Arr):
                            pass
                    # 移动后的点与蛇尾之间的距离 选出比蛇头的距离还长的点的坐标
                    #虚拟蛇尾当成食物
                    #绕食物的最远距离
                    # if manhattan_distant(next, self.board.tail_Arr[len(self.board.tail_Arr)-1]) < manhattan_distant(self.board.head,self.board.tail_Arr[len(self.board.tail_Arr)-1]):
                    #     t = self.board.is_tail_inside(next,self.board.tail_Arr[len(self.board.tail_Arr)-1])
                    #     if not t:
                    #         best_move = self.choose_shortest_safe_move()
                    #         break
                    #     else:
                    #         if manhattan_distant(next, self.board.food) > manhattan_distant(self.board.head, self.board.food):
                    #             t = self.choose_shortest_safe_move()
                    #         break
                    # else:
                    #     best_move = self.any_possible_move()
                    #     break

        return best_move


    #不能选择一个方向，则应该尝试让蛇头跟着蛇尾走
    def follow_tailArr(self):
        self.board.board_reset()
        self.board.board_refresh()
        return self.choose_longest_safe_move()


