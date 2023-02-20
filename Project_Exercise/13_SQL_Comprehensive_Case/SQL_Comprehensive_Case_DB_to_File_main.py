"""
SQL 综合案例,将MySQL数据库中的数据读取出来,并写到文件中.
"""
import json

from pymysql import Connection

# 构建MySQL数据库链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True,

)

# 获得游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("py_sql")

# 执行SQL语句,读取数据
cursor.execute("select * from orders where order_date >= '2011-02-01';")   # '2011-02-01'用这个字符串的方式大于等于的条件限制才有效.

# 接收数据
results = cursor.fetchall()
columns = [column[0] for column in cursor.description]
# print(columns)  # 输出结果:['order_date', 'order_id', 'money', 'province']

for row in results:  # 用for从results中循环遍历出row,row中的内容为每一条查询语句的结果
    # print(row)  # 输出结果:(datetime.date(2011, 2, 28), '92204883-9c91-4117-a2bd-1a05a9aba69f', 2304, '河北省')---问题在这

    print(dict(zip(columns, row)))
    # 输出结果:{'order_date': datetime.date(2011, 2, 28), 'order_id': 'e7c0797c-609c-474a-82a5-7293f93594f6', 'money': 630, 'province': '山东省'}



# 将数据进行保存到文件
## tf = open("导出2011年2月销售数据JSON.txt", "w")

# tf.write(dict)  # 这样写报错:TypeError: write() argument must be str, not type 翻译:write()参数必须是str，而不是type
## tf.write(str(dict))  # 输出的txt文件中内容只有: <class 'dict'> 这一行.
# 可能是这里的原因:'order_date': datetime.date(2011, 2, 28),

# json.dump(dict, tf)  # 报错:TypeError: Object of type type is not JSON serializable 翻译:类型错误:类型的对象不能被JSON序列化
# 可能是这里的原因:'order_date': datetime.date(2011, 2, 28),  2011, 2, 28应该为字符串即:'2011-02-28'   where order_date >= '2011-02-01'

## tf.close()

cursor.close()

# 关闭链接对象
conn.close()
