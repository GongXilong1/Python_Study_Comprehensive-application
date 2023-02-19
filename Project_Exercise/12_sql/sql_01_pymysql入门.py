"""
演示Python pymysql库的基础操作
"""

from pymysql import Connection  # 从pymysql模块导入Connection类

# 构建到MySQL数据库的链接
conn = Connection(      # 定义conn这个连接对象,通过Connection类传入以下四个参数.
    host="localhost",   # 主机名(用IP:127.0.0.1也可)
    port=3306,          # 端口
    user="root",        # 用户名
    password="123456",  # 密码
)


print(conn.get_server_info())

# 执行非查询性质SQL
cursor = conn.cursor()  # 通过conn这个连接对象调用cursor()方法获取到游标对象cursor.

# 选择数据库
conn.select_db("world")

# 执行查询性质SQL
# 执行SQL
# cursor.execute("create table test_pymysql(id int);")   # 游标对象cursor调用execute方法执行SQL语句.
cursor.execute("select * from newstu;")  # from不要打成form

results = cursor.fetchall()  # 使用游标对象的fetchall接收查询结果.  结果时双层嵌套元组.
for r in results:  # 用for从results中循环遍历出r,r中的内容为每一条查询语句的结果
    print(r)


# 关闭链接
conn.close()  # 用完连接后进行关闭


