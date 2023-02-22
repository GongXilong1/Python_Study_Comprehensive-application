"""
演示将RDD输出到文件中
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/Python3.10.2amd64/python.exe"
os.environ['HADOOP_HOME'] = "D:\Program Files\hadoop-3.0.0"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# conf.set("spark.default.parallelism", "1")  # 设置属性全局并行度为1,即分区数为1.  --方法一
sc = SparkContext(conf=conf)

# 准备RDD1
rdd1 = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)  # numSlices=1表示设置分区数为1.  --方法二

# 准备RDD2
rdd2 = sc.parallelize([("Hello", 3), ("Spark", 5), ("Hi", 7)], numSlices=1)

# 准备RDD3
rdd3 = sc.parallelize([[1, 3, 5], [6, 7, 9], [11, 13, 11]], numSlices=1)

# 输出到文件中
rdd1.saveAsTextFile("./output1")  # "./output1"这个写法会在当前目录创建output1文件夹并把rdd数据放在文件中
rdd2.saveAsTextFile("./output2")  # 不设置分区时候,文件夹会输出多个文件,数量和CPU核心数一致.
rdd3.saveAsTextFile("./output3")


sc.stop()




# saveAsTextFile依赖Hadoop大数据框架,


