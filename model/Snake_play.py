# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys, random, time
from pygame.locals import *

class Snake_paly:
    global FPSCLOCK, DISPLAY, BASICFONT, BLACK, WHITE, RED, GREY

    """ 全局变量初始化 """
    pygame.init()  # 初始化Pygame库
    DISPLAY = pygame.display.set_mode((640, 480))  # 设置分辨率
    pygame.display.set_caption('人人都是Pythonista - Snake')

    FPSCLOCK = pygame.time.Clock()  # 定义一个变量来控制游戏速度
    BASICFONT = pygame.font.SysFont("SIMYOU.TTF", 80)

    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREY = pygame.Color(150, 150, 150)

    """ 对象初始化 """
    snake_Head = [100, 100]   # 贪吃蛇的的初始位置
    snake_Body = [[80, 100], [60, 100], [40, 100]]  # 初始化贪吃蛇的长度 (注：这里以20*20为一个标准小格子)
    direction = "right"  # 指定蛇初始前进的方向，向右

    food_Position = [300, 300]  # 给定第一枚食物的位置
    food_flag = 1  # 食物标记：0代表食物已被吃掉；1代表未被吃掉

    def control_move(self):
        UP = 'up'
        DOWN = 'down'
        LEFT = 'left'
        RIGHT = 'right'

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()  # 接收到退出事件后，退出程序
                sys.exit()

            # 判断键盘事件，用 方向键 或 wsad 来表示上下左右
            elif event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_w) and direction != DOWN:  # 向上箭头或W，且direction不是向下
                    direction = UP
                if (event.key == K_DOWN or event.key == K_s) and direction != UP:  # 向下箭头或S，且direction不是向上
                    direction = DOWN
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:  # 向左箭头或A，且direction不是向右
                    direction = LEFT
                if (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:  # 向右箭头或D，且direction不是向左
                    direction = RIGHT

            # 根据键盘的输入，改变蛇的头部，进行转弯操作
            if direction == LEFT:
                self.snake_Head[0] -= 20
            if direction == RIGHT:
                self.snake_Head[0] += 20
            if direction == UP:
                self.snake_Head[1] -= 20
            if direction == DOWN:
                self.snake_Head[1] += 20

            # 将蛇的头部当前的位置加入到蛇身的列表中
                self.snake_Body.insert(0, list(self.snake_Head))

    def tellEat(self):
        # 吃掉食物
        if self.snake_Head[0] == self.food_Position[0] and self.snake_Head[1] == self.food_Position[1]:
            food_flag = 0
        else:  # 因为control_move前面加了一段
            self.snake_Body.pop()

    def generateFood(self):
        # 生成新的食物
        if self.food_flag == 0:
            # 随机生成x, y
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            food_Position = [int(x * 20), int(y * 20)]
            food_flag = 1

    def drawSnake(self, snake_Body):  # 绘制贪吃蛇
        for i in snake_Body:
            pygame.draw.rect(DISPLAY, WHITE, self.Rect(i[0], i[1], 20, 20))

    def drawFood(self, food_Position):  # 绘制食物的位置
        pygame.draw.rect(DISPLAY, RED, self.Rect(food_Position[0], food_Position[1], 20, 20))

    def drawScore(self, score):   # 打印出当前得分
        score_Surf = BASICFONT.render('%s' % (score), True, GREY)  # 设置分数的显示颜色
        score_Rect = score_Surf.get_rect()  # 设置分数的位置
        score_Rect.midtop = (320, 240)
        DISPLAY.blit(score_Surf, score_Rect)  # 绑定以上设置到句柄

    def GameOver(self): # 游戏结束并退出
        GameOver_Surf = BASICFONT.render('Game Over!', True, GREY)  # 设置GameOver的显示颜色
        GameOver_Rect = GameOver_Surf.get_rect()  # 设置GameOver的位置
        GameOver_Rect.midtop = (320, 10)
        DISPLAY.blit(GameOver_Surf, GameOver_Rect)  # 绑定以上设置到句柄

        pygame.display.flip()
        time.sleep(3)  # 等待3秒
        pygame.quit()  # 退出游戏
        sys.exit()  # 退出程序

    def main(self):
        DISPLAY.fill(BLACK)
        self.drawSnake(self.snake_Body)  # 画出贪吃蛇
        self.drawFood(self.food_Position)  # 画出食物的位置
        self.drawScore(len(self.snake_Body) - 3)  # 打印出玩家的分数
        pygame.display.flip()  # 刷新
        FPSCLOCK.tick(7)  # 控制游戏速度

        '''游戏结束的判断'''
        # 贪吃蛇触碰到边界
        if self.snake_Head[0] < 0 or self.snake_Head[0] > 620:
            self.GameOver()
        if self.snake_Head[1] < 0 or self.snake_Head[1] > 460:
            self.GameOver()
        # 贪吃蛇触碰到自己
        for i in self.snake_Body[1:]:
            if self.snake_Head[0] == i[0] and self.snake_Head[1] == i[1]:
                self.GameOver()


if __name__ == '__main__':
    sp = Snake_paly()
    sp.main()

