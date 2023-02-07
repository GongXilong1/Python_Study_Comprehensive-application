"""最后修改时间：2023.2.7--21:30"""
# 最先导入官方模块
import pygame  # 其次导入第三方模块
from plane_sprites import *  # 从plane_sprites中导入所有工具  # 最后导入应用程序模块


class PlaneGame(object):  # 定义PlaneGame类，继承自object基类，
    """飞机大战主游戏"""

    def __init__(self):  # 定义初始化方法
        print("游戏初始化")
        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(
            SCREEN_RECT.size)  # 使用self.给游戏窗口属性命名为screen，通过display模块提供的set_mode方法设置游戏窗口。
        # set_mode方法接收一个元组，SCREEN_RECT常量的size属性就是元组。

        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()  # 使用self.给时钟属性命名为clock，使用pygame中time模块中的Clock类，

        # 3. 调用私有方法，来完成精灵和精灵组的创建
        self.__create_sprites()

        # 4. 设置定时器事件-创建敌机，1秒钟出现一个。
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 700)  # 使用pygame中time模块中的set_timer方法，通过set_timer方法来创建创建敌机的事件.
        # set_timer方法需要接收两个参数，第一个是CREATE_ENEMY_EVENT这个创建敌机的常量，第二个是事件触发的间隔时间,即间隔多长时间创建一架敌机，单位是毫秒。这里设置700毫秒。

        # 5. 设置定时器事件-发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 300)  # 使用pygame中time这个模块中的set_timer方法,通过set_timer方法来创建发射子弹的事件.
        # set_timer方法需要接收两个参数，第一个是HERO_FIRE_EVENT这个创建英雄发射子弹事件的常量，第二个是事件触发的间隔时间,即发射子弹的间隔时间，单位是毫秒。这里设置300毫秒。

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
        self.back_group = pygame.sprite.Group(background1,
                                              background2)  # 创建back_group精灵组，使用pygame中的sprite模块中的Group类创建精灵组，
        # 并把background1和background2这两个精灵传递到back_group精灵组内部。

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()  # 创建enemy_group敌机的精灵组，使用pygame中的sprite模块中的Group类创建精灵组.

        # 创建英雄的精灵和精灵组
        self.hero = Hero()  # 英雄精灵需要在其他方法中使用,所以使用self.给hero的属性命名,使用Hero来创建英雄对象.
        self.hero_group = pygame.sprite.Group(
            self.hero)  # 创建hero_group英雄的精灵组，使用pygame中的sprite模块中的Group类创建精灵组,并把英雄对象self.hero传递到英雄精灵组的内部.

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
                # print("敌机出场...")  # 如果是创建敌机事件，就输出敌机出场...。
                # 创建敌机精灵
                enemy = Enemy()  # 给敌机精灵命令enemy，用Enemy类创建敌机精灵，因为敌机的图像已经封装到初始化方法中，所以不需要再指定图像位置参数了。
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)  # 用enemy_group调用add方法，add方法可以将精灵添加到精灵组。
            elif event.type == HERO_FIRE_EVENT:  # 捕获英雄发射子弹的事件,--判断事件类型是否是HERO_FIRE_EVENT这个事件.
                self.hero.fire()  # 如果是,就让英雄调用发射子弹的方法.

            # 英雄移动方式一:
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:  # 判断event.type是否是pygame.KEYDOWN事件,如果用户按下了键,再加判断event.key是否是pygame.K_RIGHT向右的方向.
            #     print("向右移动...")

        # 英雄移动方式二:使用键盘提供的方法获取键盘按键--特点:用户可以按下按键不放,
        keys_pressed = pygame.key.get_pressed()  # 使用pygame模块中key模块中get_pressed这个方法,get_pressed会返回一个按键元组,定义变量keys_pressed接收get_pressed方法的返回值.
        # 判断keys_pressed这个元组中对应的按键索引值,数值1表示按键被按下.
        if keys_pressed[pygame.K_RIGHT]:  # 判断keys_pressed这个元组对应的索引,判断用户是否按下向右的方向键.
            self.hero.speed = 3  # 使用self.找到hero的对象后修改速度,向右移动时设置为正值,为3.
        elif keys_pressed[pygame.K_LEFT]:  # 判断用户是否按下向左的方向键
            self.hero.speed = -3  # 使用self.找到hero的对象后修改速度,向左移动时设置为负值,为-3
        else:  # 如果用户按了其他方向键
            self.hero.speed = 0  # 将英雄的速度设置为0.

    def __check_collide(self):  # 定义碰撞检测这个私有方法
        # 1.子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)  # 使用pygame中的sprite模块中的groupcollide方法.并向groupcollide方法中传入参数.
        # 第一个参数传入hero.bullets英雄子弹精灵组,第二个参数传入enemy_group敌机精灵组,第三个和第四个参数都是True,因为子弹撞到敌机后子弹被销毁,敌机被子弹击中后敌机也会被销毁所以都是Ture.

        # 2. 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)  # 使用pygame中的sprite模块中的spritecollide方法.并向spritecollide方法中传入参数.
        # 第一个参数传入self.hero英雄对象,第二个参数传入enemy_group敌机精灵组,第三个参数传入True. # 定义enemies列表接收spritecollide返回值列表.

        # 判断列表是否有内容
        if len(enemies) > 0:  # 判断enemies列表的长度是否大于0,大于0即列表内有内容.
            # 让英雄牺牲
            self.hero.kill()  # 让hero对象调用kill方法.
            # 结束游戏
            PlaneGame.__game_over()  # PlaneGame类调用__game_over这个静态方法.

    def __update_sprites(self):  # 定义更新精灵组这个私有方法
        self.back_group.update()  # back_group调用update方法。
        self.back_group.draw(
            self.screen)  # back_group调用draw方法，在调用draw方法时，需要把screen这个屏幕对象当做参数传递给draw方法，因为精灵组需要知道把组内部的每个精灵绘制到哪个屏幕上。

        self.enemy_group.update()  # 让enemy_group调用update方法，更新所有敌机的位置
        self.enemy_group.draw(self.screen)  # 让enemy_group调用draw方法，需要传入屏幕对象。

        self.hero_group.update()  # 让hero_group调用update方法.
        self.hero_group.draw(self.screen)  # 让hero_group调用draw方法,并传入屏幕对象.

        self.hero.bullets.update()  # 让hero.bullets调用update方法,让子弹精灵组更新.
        self.hero.bullets.draw(self.screen)  # 让hero.bullets调用draw方法,并传入屏幕对象.

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
