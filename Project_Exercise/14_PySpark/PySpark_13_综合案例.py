"""
演示PySpark综合案例
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/Python3.10.2amd64/python.exe"
os.environ['HADOOP_HOME'] = "D:\Program Files\hadoop-3.0.0"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 读取文件转换成RDD

# TODO 需求1: 热门搜索事件端Top3(小时精度)
# 1.1 取出全部的时间并转换为小时

# 1.2 转换为(小时, 1)的二元元祖
# 1.3 Key分组聚合Value
# 1.4 排序(降序)
# 1.5 取前3

# TODO 需求2: 热门搜索词Top3

# 2.1 取出


# TODO 需求3: 统计黑马程序员关键字在什么时间段搜索的最多










