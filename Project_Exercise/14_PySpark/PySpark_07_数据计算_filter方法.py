"""
演示RDD的filter成员方法的使用
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/Python3.10.2amd64/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])

# 对RDD的数据进行过滤,偶数被保留, 奇数被抛弃
rdd2 = rdd.filter(lambda num: num % 2 == 0)        # num % 2 == 0表示num为偶数,偶数返回Ture,奇数返回False.

print(rdd2.collect())   # 运行结果:[2, 4]       --2和4被保留,1,3,5被丢弃


sc.stop()
