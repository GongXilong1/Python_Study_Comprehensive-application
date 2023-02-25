"""
演示Socket服务端开发
"""
import socket

# 创建Socket对象
socket_server = socket.socket()

# 绑定IP地址和端口
socket_server.bind(("localhost", 8888))

# 监听端口
socket_server.listen(1)  # listen方法内接受一个整数参数, 表示接受的链接数量.

# 等待客户端连接

# result = socket_server.accept()  # accept()返回的是一个二元元组.
# conn = result[0]        # conn表示的是: 客户端和服务端的链接对象,即result的[0]号元素
# address = result[1]     # address表示的是: 客户端的地址信息,即result的[1]号元素

conn, address = socket_server.accept()
# accept()返回的是一个二元元组(链接对象, 客户端地址信息).
# 可以通过 变量1, 变量2 = socket_server.accept()的形式, 直接接受二元元组内的两个元素.
# accept()方法,是阻塞的方法, 等待客户端的链接, 如果没有链接, 就卡在这一行不向下执行.

print(f"接收到了客户端的链接, 客户端的信息是: {address}")

while True:

    # 接受客服端信息, 要使用客户端和服务端的本次链接对象, 而非socket_server对象
    data: str = conn.recv(1024).decode("UTF-8")  # recv方法中传入参数1024.
    # recv接收的参数是(buffer size)缓冲区大小, 一般给1024即可.
    # recv方法的返回值是一个字节数组也就是bytes对象,不是字符串,可以通过decode方法通过UTF-8 编码,将字节数组转换为字符串对象.

    print(f"客户端发来的消息是: {data}")

    # 发送回复消息
    # msg = input("请输入你要和客户端回复的消息: ").encode("UTF-8")  # encode 可以将字符串编码为字节数组对象
    msg = input("请输入你要和客户端回复的消息: ")
    if msg == 'exit':
        break

    conn.send(msg.encode("UTF-8"))

# 关闭链接
conn.close()
socket_server.close()


# -------------
# 运行结果:
# 接收到了客户端的链接, 客户端的信息是: ('127.0.0.1', 64201)
# 客户端发来的消息是: 你好呀
#
# 请输入你要和客户端回复的消息: 你也好呀
# 客户端发来的消息是: 喜欢你呀
# 请输入你要和客户端回复的消息: 不好意思你是个好人
# 客户端发来的消息是: 不要呀
#
# 请输入你要和客户端回复的消息: 再见
# 客户端发来的消息是: 1
#
# 请输入你要和客户端回复的消息: exit
#
# 进程已结束,退出代码0

