"""
演示Python pymysql库的数据插入操作
"""

from pymysql import Connection  # 从pymysql模块导入Connection类

# 构建到MySQL数据库的链接
conn = Connection(      # 定义conn这个连接对象,通过Connection类传入以下四个参数.
    host="localhost",   # 主机名(用IP:127.0.0.1也可)
    port=3306,          # 端口
    user="root",        # 用户名
    password="123456",  # 密码
    autocommit=True     # 设置自动提交(确认),下方就不需要手动写conn.commit()
)

# print(conn.get_server_info())

# 执行非查询性质SQL
cursor = conn.cursor()  # 通过conn这个连接对象调用cursor()方法获取到游标对象cursor.

# 选择数据库
conn.select_db("world")

# 执行插入SQL
cursor.execute("insert into newstu values(10022, '林君洁', 33, '男');")  # from不要打成form

# 通过commit确认 -- 上面设置自动确认,所以这里可以不写.
# conn.commit()

# 关闭链接
conn.close()  # 用完连接后进行关闭





