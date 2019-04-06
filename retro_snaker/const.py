import pygame


# 专门放置程序中的常量
class Const:
    pass


# 创建类的对象 并写入常量
const = Const()
const.BOX = 10  # 一个格子的长和宽为20px
const.BOARD_WIDTH = 20  # 游戏的屏幕宽有多少个格子
const.BOARD_HEIGHT = 10  # 游戏的屏幕高有多少个格子
# 颜色的常量
const.BLACK_COLOR = pygame.Color(0, 0, 0)
const.RED_COLOR = pygame.Color(255, 0, 0)
const.GREEN_COLOR = pygame.Color(0, 255, 0)
const.BLUE_COLOR = pygame.Color(0, 0, 255)
const.YELLOW_COLOR = pygame.Color(255, 255, 0)
const.PURPLE_COLOR = pygame.Color(255, 0, 255)
const.CYAN_COLOR = pygame.Color(0, 255, 255)
const.WHITE_COLOR = pygame.Color(255, 255, 255)
const.GRAY_COLOR = pygame.Color(127, 127, 127)
# 移动后的状态E
const.STATE_GAMEOVER = 0  # 游戏结束
const.STATE_MOVE = 1  # 移动一格
const.STATE_EAT_FOOD = 2  # 吃到食物

# 定义棋盘中的食物 蛇头 蛇尾
const.FOOD = -1
const.SNAKE_HEAD = -2
const.SNAKE_TAIL = -3
const.UNDEFINED = const.BOARD_WIDTH * const.BOARD_HEIGHT + 1


# 两点之间的距离
# 曼哈顿距离（即两个坐标的直角距离）
def manhattan_distant(p1, p2):
    distant = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return distant
