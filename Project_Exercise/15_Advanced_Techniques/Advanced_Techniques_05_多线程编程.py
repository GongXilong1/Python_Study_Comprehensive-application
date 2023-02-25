"""
演示多线程编程的使用
"""
import time
import threading  # 导入多线程模块


def sing(msg):
    while True:  # 无限循环开启
        # print("我在唱歌, 啦啦啦...")
        print(msg)
        time.sleep(1)  # 睡眠1秒钟


def dance(msg):
    while True:
        # print("我在跳舞, 哗哗哗...")
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # 创建一个唱歌的线程
    sing_thread = threading.Thread(target=sing, args=("我要唱歌, 哈哈哈", ))  # args=("我要唱歌, 哈哈哈", )表示以元组的形式传参.
    # 创建一个跳舞的线程
    dance_thread = threading.Thread(target=dance, kwargs={"msg": "我在跳舞, 啦啦啦"})  # kwargs={"msg": "我在跳舞, 啦啦啦"}表示以字典的形式取传参.

    # 让线程干活
    sing_thread.start()
    dance_thread.start()


