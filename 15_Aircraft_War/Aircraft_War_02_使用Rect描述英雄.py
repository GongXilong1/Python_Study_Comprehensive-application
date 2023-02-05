import pygame

# pygame.Rect是一个比较特殊的类，内部只是封装了一些数字计算，不执行pygame.init()方法也同样能够直接使用。
hero_rect = pygame.Rect(100, 500, 120, 125)  # 创建矩形区域这个变量hero_rect，再使用pygame模块找到Rect这个类创建对象，并指定对象x y 宽 高。

print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))  # 输出hero_rect变量的x和y属性。
print("英雄的尺寸 %d %d" % (hero_rect.width, hero_rect.height))  # 输出hero_rect变量的width和height属性。

print("%d %d" % hero_rect.size)  # 通过hero_rect变量的size属性输出英雄的尺寸。size属性是一个元组属性，size属性的第一个值是宽度，第二个值是高度。

