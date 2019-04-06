'''
贪吃蛇小游戏
'''
import pygame
from pygame.locals import *
import sys
from const import const
from algorithm import *

from algorithm import Algorithm
from board import Board


def main():
    # 初始化棋盘
    board = Board()
    myfood = board.initFoodPos()  # 随机生成食物坐标
    board.set_food(myfood)  # 初始化食物位置
    board.set_head([0, 0])  # 初始化头部
    board.set_tailArr([])  # 初始化尾部
    direction = "right"  # 初始化方向
    # 初始化算法类
    algorithm = Algorithm(board)
    # 初始化pygame
    pygame.init()
    # 窗口大小
    SCREEN_SIZE = (const.BOARD_WIDTH * const.BOX, const.BOARD_HEIGHT * const.BOX)
    # 设置显示模式
    # 参数1 分辨率 元组 两个值
    # 参数2 标志位 如果不需要什么特效 直接写0
    # 参数3 色深
    playSurface = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    # 设置窗口标题
    pygame.display.set_caption("贪吃蛇")
    # 初始化时钟对象
    fpsClock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            # 接收到退出事件后退出程序
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # 接收键盘事件
            # if event.type == KEYDOWN:
            #     # 判断上下左右等方向
            #     if event.key == K_LEFT or event.key == ord("a"):
            #         direction = "left"
            #     elif event.key == K_RIGHT or event.key == ord("d"):
            #         direction = "right"
            #     elif event.key == K_UP or event.key == ord("w"):
            #         direction = "up"
            #     elif event.key == K_DOWN or event.key == ord("s"):
            #         direction = "down"
            #     elif event.key == K_ESCAPE:  # esc键
            #         pygame.event.post(pygame.event.Event(QUIT))

        # 蛇头移动一格
        cur_state = board.move_with_tail(direction)
        print(len(board.tail_Arr))
        # print(board.tail_Arr)
        # 绘制背景
        playSurface.fill(const.BLACK_COLOR)
        # 绘制食物
        # 参数一surface在哪个surface对象上进行绘制
        # 参数2 color颜色在pygame.Color()对象上
        # 参数3 Rect矩形
        # 食物
        pygame.draw.rect(playSurface, const.GREEN_COLOR,
                         Rect(board.food[0] * const.BOX, board.food[1] * const.BOX, const.BOX, const.BOX))
        # 蛇头
        pygame.draw.rect(playSurface, const.RED_COLOR,
                         Rect(board.head[0] * const.BOX, board.head[1] * const.BOX, const.BOX, const.BOX))
        # 蛇尾
        for position in board.tail_Arr:
            pygame.draw.rect(playSurface, const.GRAY_COLOR,
                             Rect(position[0] * const.BOX, position[1] * const.BOX, const.BOX, const.BOX))

        # 刷新pygame显示器
        pygame.display.flip()
        # 根据食物位置 蛇头位置 蛇尾位置 决定下一步移动的方向
        direction = algorithm.findDirection()
        # print(direction)
        if direction == "end":
            pygame.event.post(pygame.event.Event(QUIT))
        # 判断游戏是否结束
        if cur_state == const.STATE_GAMEOVER:
            pygame.event.post(pygame.event.Event(QUIT))
        # 控制游戏速度
        fpsClock.tick(10)


def test_is_obstacle_between():
    board = Board()
    board.set_food([5, 3])
    board.set_head([3, 1])
    board.set_tailArr([[3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [4, 2]])
    ret = board.is_obstacle_between([5, 3], [3, 1])
    print(ret)


# 测试打印棋盘和重置棋盘
def test_board_reset():
    board = Board()
    board.set_food([5, 3])
    board.set_head([2, 1])
    board.set_tailArr([[2, 0], [1, 0], [1, 1], [1, 2]])
    board.board_reset()
    board.board_print()


if __name__ == '__main__':
    main()
