"""
演示RDD的map成员方法的使用
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/Python3.10.2amd64/python.exe"  # 通过os模块中environ字典属性去设置环境变量告诉spark去哪里找Python解释器,
# 即:设置一个key 'PYSPARK_PYTHON' values是Python解释器的位置

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4 ,5])

# 通过map方法将全部数据都乘以10
# def func(data):
#     return data * 10
#
# rdd2 = rdd.map(func)  # rdd通过map方法计算func函数得到新的rdd2
# (T) -> U    (T)表示传入参数的一个鉴定,认为这里传入一个参数  U表示他有一个返回值.
# (T) -> T      表示传入一个参数,返回一个值,传入和返回值类型要一致.

# 写法二:--通过lambda匿名函数的方式
# rdd2 = rdd.map(lambda x: x * 10)  # 第一个x表示传入参数,冒号后是计算逻辑


# 链式调用 -- 实现需求:全部数据都乘以10之后再都加5      --因为返回值是rdd,所以可以一直调用算子即:.map().map()
rdd2 = rdd.map(lambda x: x * 10) .map(lambda x: x + 5)


print(rdd2.collect())

sc.stop()
