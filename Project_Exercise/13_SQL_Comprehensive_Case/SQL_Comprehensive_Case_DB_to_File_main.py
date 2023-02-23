"""
SQL 综合案例,将MySQL数据库中的数据读取出来,并写到文件中.
"""
import datetime
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
cursor.execute("select * from orders where order_date >= '2011-02-01';")  # '2011-02-01'用这个字符串的方式大于等于的条件限制才有效.

# 接收数据
results = cursor.fetchall()
columns = [column[0] for column in cursor.description]
# print(columns)  # 输出结果:['order_date', 'order_id', 'money', 'province']


result_json_lines = []
for row in results:  # 用for从results中循环遍历出row,row中的内容为每一条查询语句的结果
    # print(row)  # 输出结果:(datetime.date(2011, 2, 28), '92204883-9c91-4117-a2bd-1a05a9aba69f', 2304, '河北省')---问题在这

    json_data = {}
    for i in range(len(columns)):
        if isinstance(row[i], datetime.date):  # 判断行中是否有datetime.date格式的数据,
            json_data[columns[i]] = row[i].strftime("%Y-%m-%d")  # 有的话转成:"%Y-%m-%d" 形式
            # elif isinstance(row[i], int):
            # json_data[columns[i]] = str(row[i])

            # json_data[columns[i]] = f"丰富的{row[i]}分段{row[i]}也同样{columns[i]}"  # format举例演示  Python3.0独有
            # json_data[columns[i]] = "丰富的{0}分段{0}也同样{1}".format(row[i], columns[i])  # format举例演示   Python3.0和2.0通用
            # json_data[columns[i]] = str.format("丰富的{0}分段{0}也同样{1}", row[i], columns[i])  # format举例演示  Python3.0和2.0通用

        else:
            json_data[columns[i]] = row[i]

    # print(json_data)
    result_json = json.dumps(json_data, ensure_ascii=False)
    # print(type(result_json))
    print(result_json)
    result_json_lines.append(result_json + "\n")


# for row in results:  # --这种之前没写好的记录.
#     print(dict(zip(columns, row)))  # --合成json格式数据的简单写法.
# # 运行结果: {'order_date': datetime.date(2011, 2, 28), 'order_id': 'e7c0797c-609c-474a-82a5-7293f93594f6', 'money': 630, 'province': '山东省'}


with open("导出2011年2月销售数据JSON.txt", "w") as jf:
    jf.writelines(result_json_lines)


# json.dump(dict, tf)  # 报错:TypeError: Object of type type is not JSON serializable 翻译:类型错误:类型的对象不能被JSON序列化
# 可能是这里的原因:'order_date': datetime.date(2011, 2, 28),  2011, 2, 28应该为字符串即:'2011-02-28'   where order_date >= '2011-02-01'


cursor.close()

# 关闭链接对象
conn.close()

"""
json格式文件和python中的字典有哪些区别:
1. json中的引号都必须时双引号,字典中双引号或者单引号都可以.
2. json中Ture和False都要是小写.
"""
