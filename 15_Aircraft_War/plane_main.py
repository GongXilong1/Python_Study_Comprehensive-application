"""最后修改时间：2023.2.6--22:00"""
import pygame
from plane_sprites import *  # 从plane_sprites中导入所有工具


class PlaneGame(object):  # 定义PlaneGame类，继承自object基类，
    """飞机大战主游戏"""

    def __init__(self):  # 定义初始化方法
        print("游戏初始化")
        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)  # 使用self.给游戏窗口属性命名为screen，通过display模块提供的set_mode方法设置游戏窗口。
        # set_mode方法接收一个元组，SCREEN_RECT常量的size属性就是元组。

        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()  # 使用self.给时钟属性命名为clock，使用pygame中time模块中的Clock类，

        # 3. 调用私有方法，来完成精灵和精灵组的创建
        self.__create_sprites()

        # 4. 设置定时器事件-创建敌机，1秒钟出现一个。
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)  # 使用pygame中time这个模块中的set_timer方法，
        # set_timer方法需要接收两个参数，第一个是CREATE_ENEMY_EVENT这个创建敌机的常量，第二个是间隔多长时间创建一架飞机，单位是毫秒。这里设置1000毫秒。

    def __create_sprites(self):  # 定义私有方法__create_sprites
        # 创建背景精灵和精灵组-方法一：
        # background1 = Background("./images/background.png")  # 创建背景精灵background1，并通过Background类指定图像位置。p489视频涉及到。
        # background2 = Background("./images/background.png")  # 创建背景精灵background2，并通过Background类指定图像位置。
        # background2.rect.y = -background2.rect.height  # 指定第二张背景精灵的初始位置即在屏幕的正上方，即让y值初始等于背景图像的高度。
        # self.back_group = pygame.sprite.Group(background1, background2)  # 创建back_group精灵组，使用pygame中的sprite模块中的Group类创建精灵组，
        # 并把background1和background2这两个精灵传递到back_group精灵组内部。

        # 创建背景精灵和精灵组-方法二：--配合plane_sprites文件中Background类中初始化方法去使用。
        background1 = Background()
        background2 = Background(True)  # 传入参数Ture，表示background2是交替图像。
        self.back_group = pygame.sprite.Group(background1, background2)  # 创建back_group精灵组，使用pygame中的sprite模块中的Group类创建精灵组，
        # 并把background1和background2这两个精灵传递到back_group精灵组内部。

    def start_game(self):  # 定义start_game方法
        print("游戏开始...")
        while True:  # 游戏循环，无限循环
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)  # 使用之前创建的clock时钟对象调用tick方法，并且使用FRAME_PER_SEC刷新帧率这个常量。
            # 2. 事件监听
            self.__event_handler()  # 使用self.调用__event_handler这个私有方法
            # 3. 碰撞检测
            self.__check_collide()  # 使用self.调用__check_collide这个私有方法
            # 4. 更新/绘制精灵组
            self.__update_sprites()  # 使用self.调用__update_sprites这个私有方法
            # 5. 更新显示
            pygame.display.update()  # 使用pygame中的display模块提供的update方法更新显示。

    def __event_handler(self):  # 定义事件监听这个私有方法
        for event in pygame.event.get():  # 使用pygame中event模块调用get方法，get方法会返回当前这一时刻发生的所有事件列表，
                                            # 使用for循环监听事件，定义变量event
            # 判断是否退出游戏
            if event.type == pygame.QUIT:  # 要判断事件类型就用event.type获取事件类型，并用if判断是否为pygame.QUIT定义的退出事件。
                PlaneGame.__game_over()  # 用类名.的方式调用静态方法。
            elif event.type == CREATE_ENEMY_EVENT:  # 使用elif判断事件类型，判断事件类型是否是CREATE_ENEMY_EVENT。
                print("敌机出场...")  # 如果是创建敌机事件，就输出敌机出场...。

    def __check_collide(self):  # 定义碰撞检测这个私有方法
        pass

    def __update_sprites(self):  # 定义更新精灵组这个私有方法
        self.back_group.update()  # back_group调用update方法。
        self.back_group.draw(self.screen)  # back_group调用draw方法，在调用draw方法时，需要把screen这个屏幕对象当做参数传递给draw方法，因为精灵组需要知道把组内部的每个精灵绘制到哪个屏幕上。

    @staticmethod
    def __game_over():  # 定义游戏结束这个私有方法   这个方法中没有使用到对象的属性，没有使用到类属性，所以可以把这个方法定义成静态方法。
        print("游戏结束")

        pygame.quit()  # 让pygame调用quit方法，卸载所有的模块。
        exit()  # 调用系统的exit函数，终止当前正在执行的程序，


# 当敲下main时，智能提示会自动写出if __name__ == '__main__':这句代码。
if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()  # 游戏对象命名：game，用PlaneGame类创建游戏对象
    # 启动游戏
    game.start_game()  # 让游戏对象game调用start_game这个方法。







