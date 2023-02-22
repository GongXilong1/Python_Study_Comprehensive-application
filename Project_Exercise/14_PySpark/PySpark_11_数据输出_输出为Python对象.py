"""
演示将RDD输出为Python对象
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/Python3.10.2amd64/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
# print(rdd)  # 运行结果:ParallelCollectionRDD[0] at readRDDFromFile at PythonRDD.scala:274

# collect算子,输出RDD为list对象
rdd_list: list = rdd.collect()
# print(rdd_list)  # 运行结果:[1, 2, 3, 4, 5]
# print(type(rdd_list))  # 运行结果:<class 'list'>

# reduce算子,对RDD进行两两聚合
num = rdd.reduce(lambda a, b: a + b)
# print(num)  # 运行结果: 15

# take算子,取出RDD前N个元素,组成list返回
take_list = rdd.take(3)
# print(take_list)  # 运行结果: [1, 2, 3]

# count, 统计rdd内有多少条数据,返回值为数字
num_count = rdd.count()
print(f"rdd内有{num_count}个元素")  # 运行结果: rdd内有5个元素


sc.stop()
