"""
演示RDD的sortBy成员方法的使用
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/Program Files/Python3.10.2amd64/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 1. 读取数据文件
rdd = sc.textFile("./hello.txt")

# 2. 取出全部单词  rdd对象调用flatMap算子用空格方式将每个单词分隔开.
word_rdd = rdd.flatMap(lambda x: x.split(" "))

# 3. 将所有单词都转换成二元元组,单词为Key, value设置为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))        # 每一个单词(这句中第一个word)传进来,返回一个二元元组,word作为key,1为value. 定义word_with_one_rdd接收二元元组.

# 4. 分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b: a + b)       # a, b: a + b为累加逻辑,先a b 分组,然后组内相加.

# print(result_rdd.collect())
# 运行结果:[('itcast', 4), ('python', 6), ('itheima', 7), ('spark', 4), ('pyspark', 3)]

# 5. 对结果进行排序,按照出现次数多的在前,即按照二元元组的第二个元素的大小进行排序.
final_rdd = result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
# 定义final_rdd接收返回值,result_rdd调用sortBy算子,lambda x: x[1]表示按照二元元组的[1]位元素(第二个元素)进行排序,ascending=False表示降序(Ture为升序),numPartitions=1表示分区数为1.

print(final_rdd.collect())
# 运行结果:[('itheima', 7), ('python', 6), ('itcast', 4), ('spark', 4), ('pyspark', 3)]

sc.stop()




