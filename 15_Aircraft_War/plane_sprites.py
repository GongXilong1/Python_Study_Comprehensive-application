"""最后修改时间：2023.2.7--21:30"""
import random  # 最先导入官方模块
import pygame  # 其次导入第三方模块
# 最后导入应用程序模块

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)  # 定义屏幕大小的常量SCREEN_RECT，使用pygame的Rect类创建一个矩形对象，参数 x y 宽 高，

# 刷新的帧率
FRAME_PER_SEC = 60  # 定义刷新帧率这个常量，并设置为60。

# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT  # 定义CREATE_ENEMY_EVENT常量，指定常量值，通过pygame中的USEREVENT。

# 英雄发射子弹事件常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1  # 定义常量名HERO_FIRE_EVENT,指定常量值:让pygame中的USEREVENT+1,形成新的整数常量.


class GameSprite(pygame.sprite.Sprite):  # 定义类名GameSprite，在小括号中指定游戏精灵的父类，即pygame的sprite模块中的Sprite类
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):  # 通过def关键字 定义 init 初始化方法，增加两个形参，第一个是image_name，第二个是speed，并且有一个初始值1。

        # 调用父类的初始化方法
        super().__init__()  # 用super这个对象来调用父类的初始化方法。

        # 定义对象的属性，定义游戏精灵的三个属性：image、rect、speed

        # self.image = pygame.image.load("./images/background.png")
        # 如果用上面这句直接指定图像目录的方式，在plane_main.py文件中创建背景精灵和精灵组方法一部分中的：background1 = Background("")这句就可以不写图像路径了。

        self.image = pygame.image.load(image_name)  # 视频p480中涉及这句。使用self.定义image属性。
        # 要想在图像文件中加载数据，可以使用pygame.images模块调用load方法，把传入的image_name当做参数传递给这个方法。这样就可以把指定名称的图像加载到图像属性中了。

        self.rect = self.image.get_rect()  # 使用self.定义rect属性，如果rect属性默认大小是图像的大小，可以让image调用get_rect方法。
        self.speed = speed  # 使用self.定义speed属性，并把形参speed传递过来。

    def update(self):  # 重写父类的update方法，在新的update方法中让游戏精灵在垂直方向上运动。
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed  # 修改self.rect属性中的y属性，让y属性加上self.speed属性


# 强调：在开发子类的时候，如果子类的父类不是object这个基类，那么在初始化方法中，需要主动调用父类的初始化方法。
# 因为不主动调用父类的初始化方法，就没办法享受到父类中已经封装好的super().__init__()这个初始化代码。


class Background(GameSprite):  # 定义Background背景类，让Background类继承自GameSprite这个子类
    """游戏背景精灵"""

    def __init__(self, is_alt=False):  # 定义初始化方法，并增加is_alt参数，并且设置默认值为False，默认值为False就表示创建出来的背景正好是叠加在屏幕上方的。
        # 1.调用父类方法实现精灵的创建，父类方法中可以设置image/rect/speed，所以可以直接调用父类方法来完成精灵的基本属性设置。
        super().__init__("./images/background.png")  # 使用super这个特殊类，类名后加（）来创建出一个特殊的对象super，由super这个对象来调用初始化方法，并且指定背景精灵要显示的图像目录。
        # 2.判断is_alt这个参数，判断是否是交替图像，如果是，需要设置初始位置。
        if is_alt:
            self.rect.y = -self.rect.height  # 如果为真，就表示是交替图像，既然是交替图像，就要设置self.rect的y值，让self.rect的y值等于负的图像高度。

    def update(self):  # 重写父类（GameSprite）的update方法
        # 1. 调用父类的方法实现垂直移动
        super().update()  # 使用super这个特殊的类调用父类的update方法。

        # 2. 判断是否移出屏幕，如果移出屏幕，应该将图像设置到屏幕的上方。
        if self.rect.y >= SCREEN_RECT.height:  # 判断self.rect的y值是否大于等于SCREEN_RECT的高度，如果大于，就认为图像已经移出屏幕。
            self.rect.y = -self.rect.height  # 如果图像移出屏幕，就应该将图像设置到屏幕的上方，即把self.rect的y值设置成图像高度的负值。


class Enemy(GameSprite):  # 定义Enemy敌机精灵类，让Background类继承自GameSprite这个子类
    """敌机精灵"""
    def __init__(self):  # 定义初始化方法

        # 1. 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")  # 使用super这个特殊类调用父类方法，调用父类的初始化方法的同时就可以指定敌机精灵图像的目录位置。

        # 2. 指定敌机的初始随机速度 1-3
        self.speed = random.randint(1, 3)  # 使用self.找到speed属性，使用random模块调用randint方法，randint方法可以接收两个参数，第一参数是随机数的最小值，第二个参数是随机数的最大值。

        # 3. 指定敌机的初始随机位置
        self.rect.bottom = 0  # 这句是设置y方向的初始位置，用self.调用rect属性中的bottom属性，并设置初始值为0，这样敌机的初始位置会在屏幕框的上方，让飞机进入屏幕的效果更加平滑自然。

        max_x = SCREEN_RECT.width - self.rect.width  # 定义max_x这个局部变量，让max_x这个变量等于游戏屏幕的宽度减去当前敌机图像的宽度，max_x变量即敌机出现的最大X值。
        self.rect.x = random.randint(0, max_x)  # 这句是设置敌机图像在x方向的初始位置。使用使用self.找到rect属性的x属性，使用random模块调用randint方法来设置初始X值，
        # randint方法中接收两个参数，第一个参数是最小x值为0，第二个参数是最大x值为max_x。

    def update(self):
        # 1. 调用父类方法，保持垂直方向的飞行，因为GameSprite这个父类中已经实现了垂直方向的飞行
        super().update()  # 使用super这个特殊对象调用父类的update方法。
        
        # 2. 判断是否飞出屏幕，如果是飞出屏幕，需要从精灵组删除敌机。
        if self.rect.y >= SCREEN_RECT.height:  # 使用if判断self.rect的y值是否大于等于屏幕的高度值即SCREEN_RECT.height。
            # print("飞出屏幕，需要从精灵组删除...")  # 如果大于，就认为飞出屏幕。
            # kill方法可以将精灵从所有精灵组中移出，精灵就会被自动销毁。
            self.kill()  # 让敌机精灵自己调用kill方法。kill方法会把精灵从所有的精灵组中删除。

    def __del__(self):  # 重新定义del这个内置方法
        # print("敌机挂了 %s" % self.rect)  # 输出敌机挂了的位置，可以知道敌机在屏幕的什么位置被销毁的，
        pass


class Hero(GameSprite):  # 用class关键字定义Hero类，让Hero类继承自GameSprite这个父类
    """英雄精灵"""
    def __init__(self):  # 定义初始化方法
        # 1. 调用父类方法,设置image&speed,英雄精灵创建完成.
        super().__init__("./images/me1.png", 0)  # 使用super这个特殊类调用父类方法，调用父类的初始化方法的同时指定英雄图像目录位置。并且指定英雄的初始速度为0.

        # 2. 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx  # 此句是设置x方向的初始位置,使用self.rect属性中centerx属性 等于SCREEN_RECT.centerx 屏幕尺寸的centerx.
        self.rect.bottom = SCREEN_RECT.bottom - 120  # 此句是设置y方向的初始位置,使用self.rect属性中centerx属性bottom属性等于SCREEN_RECT的bottom属性值减去120.

        # 3. 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()  # 定义子弹精灵组名称为bullets,通过pygame模块中sprite模块的Group类来创建.

    def update(self):  # 重写update方法
        # 英雄在水平方向移动
        self.rect.x += self.speed  # 使用self.找到rect属性中x属性,让其加等于self.speed,即让英雄的x和英雄的速度叠加.

        # 控制英雄不能离开游戏屏幕
        if self.rect.x < 0:  # 判断self.rect属性中x值是否小于0,如果x小于0,说明英雄从屏幕左侧飞出.
            self.rect.x = 0  # 当self.rect属性中x值是否小于0时,就把self.rect属性中x值重新设置为0.这样英雄就无法从屏幕左侧飞出.
        elif self.rect.right > SCREEN_RECT.right:  # right属性值为x值和width值的和,判断英雄精灵的right是否大于屏幕SCREEN_RECT的right.
            self.rect.right = SCREEN_RECT.right  # 如果大于,那就再次设置为英雄精灵的right等于屏幕SCREEN_RECT的right.

    def fire(self):  # 定义发射子弹方法
        print("发射子弹...")

        for i in (0, 1, 2):  # 定义变量i,使用for循环对元组(0, 1, 2)进行遍历
            # 1. 创建子弹精灵
            bullet = Bullet()  # 通过Bullet类创建子弹精灵名字为bullet

            # 2. 设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20  # 用bullet找到rect属性中的bottom属性,使用bottom属性设置垂直方向的位置,
            # 目的是让子弹在英雄的上方,即让英雄的y值减去变量i的三个值分别与20相乘的结果,达到一次发三颗子弹的效果.
            bullet.rect.centerx = self.rect.centerx  # 设置子弹在水平方向的位置:让子弹的水平中心点和英雄的水平中心点保持一致.

            # 3. 将精灵添加到精灵组
            self.bullets.add(bullet)  # 让bullets精灵组调用add方法将子弹精灵bullet添加到精灵组.即让bullet当做参数传递给add方法.

        # 以下一段注释为发射单颗子弹的写法:
        # # 1. 创建子弹精灵
        # bullet = Bullet()  # 通过Bullet类创建子弹精灵名字为bullet
        #
        # # 2. 设置精灵的位置
        # bullet.rect.bottom = self.rect.y - 10  # 用bullet找到rect属性中的bottom属性,使用bottom属性设置垂直方向的位置,目的是让子弹在英雄的上方,即让英雄的y值减去20像素.
        # bullet.rect.centerx = self.rect.centerx  # 设置子弹在水平方向的位置:让子弹的水平中心点和英雄的水平中心点保持一致.
        #
        # # 3. 将精灵添加到精灵组
        # self.bullets.add(bullet)  # 让bullets精灵组调用add方法将子弹精灵bullet添加到精灵组.即让bullet当做参数传递给add方法.


class Bullet(GameSprite):  # 用class关键字定义Bullet类，让Bullet类继承自GameSprite这个父类
    """子弹精灵"""

    def __init__(self):  # 定义初始化方法
        # 调用父类方法,设置子弹图片,设置初始速度
        super().__init__("./images/bullet1.png", -2)  # 使用super这个特殊类调用父类方法，调用父类的初始化方法的同时指定子弹图像目录位置。并且指定子弹的初始速度为-3.

    def update(self):  # 定义update方法
        # 调用父类方法,让子弹沿垂直方向飞行
        super().update()  # # 使用super这个特殊类调用父类的update方法,因为父类的update方法中精灵就是沿着垂直方向飞行的.
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:  # 判断子弹的rect位置属性中bottom属性是否小于0.如果bottom小于0,说明子弹已经飞出屏幕.
            self.kill()  # 让子弹精灵自己调用kill方法。kill方法会把子弹精灵从所有的子弹精灵组中删除。

    def __del__(self):  # 重写del这个内置方法
        print("子弹被销毁...")


