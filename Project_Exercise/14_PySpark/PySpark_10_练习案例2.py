"""
完成练习案例: JSON商品统计
需求:
1. 各个城市销售额排名,从大到小
2. 全部城市,有哪些商品类别在售卖
3. 北京市有哪些商品类别在售卖
"""
from pyspark import SparkConf, SparkContext
import json
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/Python3.10.2amd64/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# TODO 需求1:城市销售额排名
# 1.1 读取文件得到RDD
file_rdd = sc.textFile("./orders.txt")

# 1.2 取出一个个JSON 字符串
json_str_rdd = file_rdd.flatMap(lambda x: x.split("|"))

# 1.3 将一个个JSON字符串转换为字典
dict_rdd = json_str_rdd.map(lambda x: json.loads(x))
# print(dict_rdd.collect())
# 运行结果:
# [{'id': 1, 'timestamp': '2019-05-08T01:03.00Z', 'category': '平板电脑', 'areaName': '北京', 'money': '1450'},
# {'id': 2, 'timestamp': '2019-05-08T01:01.00Z', 'category': '手机', 'areaName': '北京', 'money': '1450'}, ......]

# 1.4 取出城市和销售额数据
# 去组成(城市, 销售额)这样的二元元组, 然后对城市进行分组,对销售额进行求和
city_with_money_rdd = dict_rdd.map(lambda x: (x['areaName'], int(x['money'])))  # money值转换成int类型方便后续计算.

# 1.5 按城市分组 按销售额聚合
city_result_rdd = city_with_money_rdd.reduceByKey(lambda a, b: a + b)

# 1.6 按销售额聚合结果进行排序
result_rdd = city_result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)

print("需求1的结果是: ", result_rdd.collect())
# 运行结果: 需求1的结果是:  [('北京', 91556), ('杭州', 28831), ('天津', 12260), ('上海', 1513), ('郑州', 1120)]


# TODO 需求2: 全部城市有哪些商品类别在售卖
# 2.1 取出全部的商品类别                 # 2.2 对全部商品类别进行去重
category_rdd = dict_rdd.map(lambda x: x['category']).distinct()

print("需求2的结果: ", category_rdd.collect())
# 运行结果: 需求2的结果:  ['平板电脑', '家电', '书籍', '手机', '电脑', '家具', '食品', '服饰']


# TODO 需求3: 北京市有哪些商品类别在售卖
# 3.1 过滤北京市的数据
beijing_data_rdd = dict_rdd.filter(lambda x: x['areaName'] == '北京')

# 3.2 取出全部商品类别              # 3.3 进行商品类别去重
result3_rdd = beijing_data_rdd.map(lambda x: x['category']).distinct()

print("需求3的结果: ", result3_rdd.collect())
# 运行结果: 需求3的结果:  ['平板电脑', '家电', '书籍', '手机', '电脑', '家具', '食品', '服饰']


sc.stop()



