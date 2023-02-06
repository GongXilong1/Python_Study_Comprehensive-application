"""最后修改时间：2023.2.6--18:00"""
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)  # 定义屏幕大小的常量SCREEN_RECT，使用pygame的Rect类创建一个矩形对象，参数 x y 宽 高，

# 刷新的帧率
FRAME_PER_SEC = 60  # 定义刷新帧率这个常量，并设置为60。


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





