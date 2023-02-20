"""
SQL 综合案例,读取文件,写入MySQL数据库中
"""

from SQL_Comprehensive_Case_file_define import TextFileReader, JsonFileReader
from SQL_Comprehensive_Case_data_define import Record
from pymysql import Connection

text_file_reader = TextFileReader("./2011年1月销售数据.txt")
json_file_reader = JsonFileReader("./2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()  # list[Record]类型注解
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并为一个list来存储
all_data: list[Record] = jan_data + feb_data

# 构建MySQL数据库链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)

# 获得游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("py_sql")

# 组织SQL语句
for record in all_data:  # 通过for循环从all_data中拿到数据放到record中
    sql = f"insert into orders(order_date, order_id, money, province) " \
          f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')"
    # '{record.date}', '{record.order_id, '{record.province}'是字符串所以需要用单引号引起来.
    # print(sql)  # 输出结果显示已经完成insert语句的封装.

    # 执行SQL语句
    cursor.execute(sql)  # 通过cursor游标对象的execute执行方法把sql语句传进去.

# 关闭MySQL链接对象
conn.close()
