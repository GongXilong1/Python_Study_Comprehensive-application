"""
演示通过PySpark代码加载数据,即数据输入
"""
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# # 通过parallelize方法将Python对象加载到Spark内,成为RDD对象  ---RDD(Resilient Distributed Datasets):弹性分布式数据集
# rdd1 = sc.parallelize([1, 2, 3, 4, 5, 6])  # sc对象调用parallelize方法传入列表
# rdd2 = sc.parallelize((1, 2, 3, 4, 5))  # sc对象调用parallelize方法传入元组
# rdd3 = sc.parallelize("abcdefg")  # sc对象调用parallelize方法字符串
# rdd4 = sc.parallelize({1, 2, 3, 4, 5})  # sc对象调用parallelize方法传入集合
# rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})  # # sc对象调用parallelize方法传入字典
#
# # 如果要查看RDD里面有什么内容,需要用collect()方法.
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())


# 用多textFile方法,读取文件数据加载到Spark内,成为RDD对象
rdd = sc.textFile("./hello.txt")
print(rdd.collect())


sc.stop()



"""
--------print运行结果:
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5]
['a', 'b', 'c', 'd', 'e', 'f', 'g']    ---- 字符串会把每个字符拆出来之后存入到RDD中
[1, 2, 3, 4, 5]
['key1', 'key2']    --字典只有key进入到RDD中

Process finished with exit code 0
"""
