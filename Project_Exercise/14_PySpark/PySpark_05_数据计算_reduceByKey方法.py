"""
演示RDD的reduceByKey成员方法的使用
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/Python3.10.2amd64/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([('男', 99), ('男', 88), ('女', 98), ('女', 66)])

# 求男生和女生两个组的成绩之和
rdd2 = rdd.reduceByKey(lambda a, b: a + b)      # 通过lambda匿名函数的方式

# 完整函数方式  --算法还需要再想出来
# def func():
#     return a, b: a + b
#
# rdd2 = rdd.reduceByKey(func)

print(rdd2.collect())       # 运行结果:[('男', 187), ('女', 164)]


sc.stop()
