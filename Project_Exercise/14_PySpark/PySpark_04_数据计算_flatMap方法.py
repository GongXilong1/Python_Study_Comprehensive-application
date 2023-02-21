"""
演示RDD的flatMap成员方法的使用
"""

from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/Python3.10.2amd64/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize(["Jason Jason_test1 666", "itjason it666", "python ittest"])

# 需求,将RDD数据里的一个单词提取出来

# rdd2 = rdd.map(lambda x: x.split(" "))        # 先用map尝试效果
# print(rdd2.collect())
# 运行结果:[['Jason', 'Jason_test1', '666'], ['itjason', 'it666'], ['python', 'ittest']]

rdd2 = rdd.flatMap(lambda x: x.split(" "))      # 用flatmap算子,解除['itjason', 'it666']这一层嵌套
print(rdd2.collect())
# 运行结果:['Jason', 'Jason_test1', '666', 'itjason', 'it666', 'python', 'ittest']

sc.stop()
