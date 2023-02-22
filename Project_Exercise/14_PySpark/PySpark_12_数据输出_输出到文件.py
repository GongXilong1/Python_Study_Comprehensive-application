"""
演示将RDD输出到文件中
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/Python3.10.2amd64/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备RDD1
rdd1 = sc.parallelize([1, 2, 3, 4, 5])

# 准备RDD2
rdd2 = sc.parallelize([("Hello", 3), ("Spark", 5), ("Hi", 7)])

# 准备RDD3
rdd3 = sc.parallelize([[1, 3, 5], [6, 7, 9], [11, 13, 11]])

# 输出到文件中
rdd1.saveAsTextFile("./output1")
# rdd2.saveAsTextFile("./output2")
# rdd3.saveAsTextFile("./output3")


sc.stop()


# saveAsTextFile依赖Hadoop大数据框架,


