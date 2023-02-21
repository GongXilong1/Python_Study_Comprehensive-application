"""
完成练习案例:单词计数统计
"""

# 1. 构建执行环境入口对象
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/Python3.10.2amd64/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 2. 读取数据文件
rdd = sc.textFile("./hello.txt")

# 3. 取出全部单词  rdd对象调用flatMap算子用空格方式将每个单词分隔开.
word_rdd = rdd.flatMap(lambda x: x.split(" "))

# print(word_rdd.collect())
# 运行结果:['itheima', 'itheima', 'itcast', 'itheima', 'spark', 'python', 'spark',
# 'python', 'itheima', 'itheima', 'itcast', 'itcast', 'itheima', 'python', 'python',
# 'python', 'spark', 'pyspark', 'pyspark', 'itheima', 'python', 'pyspark', 'itcast', 'spark']

# 4. 将所有单词都转换成二元元组,单词为Key, value设置为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))        # 每一个单词(这句中第一个word)传进来,返回一个二元元组,word作为key,1为value. 定义word_with_one_rdd接收二元元组.

# print(word_with_one_rdd.collect())
# 运行结果:[('itheima', 1), ('itheima', 1), ('itcast', 1), ('itheima', 1), ('spark', 1), ('python', 1), ('spark', 1), ('python', 1),
# ('itheima', 1), ('itheima', 1), ('itcast', 1), ('itcast', 1), ('itheima', 1), ('python', 1), ('python', 1), ('python', 1), ('spark', 1),
# ('pyspark', 1), ('pyspark', 1), ('itheima', 1), ('python', 1), ('pyspark', 1), ('itcast', 1), ('spark', 1)]

# 5. 分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b: a + b)       # a, b: a + b为累加逻辑,先a b 分组,然后组内相加.

# 6. 打印输出结果
print(result_rdd.collect())
# 运行结果:[('itcast', 4), ('python', 6), ('itheima', 7), ('spark', 4), ('pyspark', 3)]


sc.stop()

