import pygame

# 游戏的初始化
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
# pygame.display.update()  # display模块下的update方法
# 不调用update方法，图像不会被绘制。


# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")  # 定义hero变量接收load方法的返回结果。调用image模块中的load方法，load方法内是要加载图像的完整路径。
screen.blit(hero, (150, 500))  # screen对象调用blit方法，blit方法可以接收两个参数，第一个是刚刚加载的图像，第一个参数是元组，元组的第一个数值是水平方向的坐标，第二个数值是竖直方向的坐标。

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()  # 定义时钟对象clock，使用pygame的time模块下的Clock这个类，

# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)   # 定义变量hero_rect记录飞机初始位置，使用pygame里的Rect类，指定 x y 宽 高 四个参数 。

# 游戏循环 -> 意味着游戏的正式开始
i = 0

while True:  # 创建while的无限循环，保证游戏不会立即退出，窗口一致显示。
    # tick方法可以指定循环体内部的代码执行的频率。
    clock.tick(60)  # 让时钟对象调用tick方法，60表示while无限循环内部的代码每秒钟重复执行60次。

    # 捕获事件  捕获用户的具体操作
    # event_list = pygame.event.get()  # 通过pygame的event模块调用get方法，get方法返回的类型是列表类型，定义变量event_list 来接收get方法返回的列表结果。
    # if len(event_list) > 0:  # 判断event_list中是否有事件发生，即event_list这个列表的长度是否为0，有事件发生后才有event_list输出。
    #     print(event_list)  # 输出event_list列表。

    # 监听事件
    for event in pygame.event.get():  # 通过for循环遍历pygame中event模块中的get方法

        # 判断事件类型是否是退出事件，退出事件是用户点击了关闭按钮。
        if event.type == pygame.QUIT:  # 判断event变量的类型是否为退出事件
            print("游戏退出...")

            # quit 如果是退出事件，就卸载掉pygame的所有的模块
            pygame.quit()  # 调用pygame的quit方法。

            # exit()   直接终止停止当前正在执行的程序
            exit()  # 调用Python的exit函数，使用exit方法是为了跳出所有循环，直接终止停止当前正在执行的程序，如果使用break，只能跳出if这种就近的循环。

    # 2. 修改飞机的位置
    hero_rect.y -= 1  # 对hero_rect这个变量的y属性执行 -= 的操作
    # 判断飞机的位置
    if hero_rect.y <= -126:  # 判断hero_rect的y值是否小于等于-126，目的是让英雄飞机完全飞出窗口，即飞机的尾部飞出窗口，126是英雄飞机的height值。
        hero_rect.y = 700   # 通过修改hero_rect的y属性修改飞机的位置。

    # 方法二：让英雄飞机完全飞出窗口
    # if hero_rect.y + hero_rect.height <= 0:  # 判断hero_rect的y属性值和hero_rect的height值之和是否小于0，目的是让英雄飞机完全飞出窗口。
    #     hero_rect.y = 700  # 通过修改hero_rect的y属性修改飞机的位置。

    # 3. 调用blit方法绘制图像
    screen.blit(background, (0, 0))  # 使用screen对象调用blit方法，把游戏背景重新绘制在0,0这个位置，解决飞机残影问题。
    screen.blit(hero, hero_rect)  # 使用screen对象调用blit方法，blit方法接收两个参数，第一个参数是要绘制的图像，第二个参数是可以传入一个坐标元组，也可以传入一个矩形对象。
    # 4. 调用update方法更新显示
    pygame.display.update()

    print(i)
    i += 1
    pass

pygame.quit()
























