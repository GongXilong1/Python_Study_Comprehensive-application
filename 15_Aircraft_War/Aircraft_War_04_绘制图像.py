import pygame

pygame.init()

# 创建游戏的窗口 ，窗口尺寸期望大小：480*700
screen = pygame.display.set_mode((480, 700))  # 使用display这个模块，没有智能提示。
# display这个模块下的set_mode方法，set_mode方法中的三个参数可以不用传递，set_mode方法返回结果就是游戏窗口，定义screen变量来接收set_mode方法返回结果。
# set_mode方法默认是创建跟屏幕一样大的窗口。set_mode方法的第一参数resolution是元组类型，用于指定窗口的宽和高。

# 绘制背景图像
# 1> 加载图像数据
background = pygame.image.load("./images/background.png")  # image模块下的load方法，在load方法内部传入要加载的图像名称。.表示当前目录，
# 定义background变量接收load方法的返回结果。

# 2> blit 绘制图像
screen.blit(background, (0, 0))  # screen对象调用blit方法，把刚刚加载的background变量传递进来，后面跟上元组，指定图像绘制的位置，

# 3> update 更新屏幕的显示
pygame.display.update()  # display模块下的update方法
# 不调用update方法，图像不会被绘制。


# 游戏循环
while True:  # 创建while的无限循环，保证游戏不会立即退出，窗口一致显示。
    pass

pygame.quit()





