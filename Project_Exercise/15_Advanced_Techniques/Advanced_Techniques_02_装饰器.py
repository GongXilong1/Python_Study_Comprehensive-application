"""
演示装饰器的写法
"""


# 装饰器的一般写法(闭包)
# def outer(func):
#     def inner():
#         print("我睡觉了")
#         func()
#         print("我起床了")
#     return inner
#
#
# def sleep():
#     import random
#     import time
#     print("睡眠中......")
#     time.sleep(random.randint(1, 5))  # 使用time模块中的sleep类让程序在这里暂停,暂停时间为随机1-5秒
#
#
# fn = outer(sleep)  # fn是outer的返回值,outer返回值返回的是inner函数
# fn()


# 装饰器的快捷写法(语法糖)
def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起床了")
    return inner


@outer  # 本质上是把sleep函数当做参数传入到outer函数中了,return了inner,inner函数执行三句睡觉代码,
def sleep():
    import random
    import time
    print("睡眠中......")
    time.sleep(random.randint(1, 5))  # 使用time模块中的sleep类让程序在这里暂停,暂停时间为随机1-5秒


sleep()  # 当前调用sleep,本质上还是调用了inner函数


