"""
演示RDD的distinct成员方法的使用
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/Python3.10.2amd64/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 1, 3, 3, 5, 5, 7, 8, 8, 9, 10])

# 对RDD的数据进行去重
rdd2 = rdd.distinct()  # distinct()算子不需要传入参数即可去重

print(rdd2.collect())  # 运行结果:[8, 1, 5, 9, 10, 3, 7]


sc.stop()

