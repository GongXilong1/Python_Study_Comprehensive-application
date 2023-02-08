import pygame

pygame.init()

# 创建游戏的窗口 ，窗口尺寸期望大小：480*700
screen = pygame.display.set_mode((480, 700))  # 使用display这个模块，没有智能提示。
# display这个模块下的set_mode方法，set_mode方法中的三个参数可以不用传递，set_mode方法返回结果就是游戏窗口，定义screen变量来接收set_mode方法返回结果。
# set_mode方法默认是创建跟屏幕一样大的窗口。set_mode方法的第一参数resolution是元组类型，用于指定窗口的宽和高。

# 游戏循环
while True:  # 创建while的无限循环，保证游戏不会立即退出，窗口一致显示。
    pass

pygame.quit()


