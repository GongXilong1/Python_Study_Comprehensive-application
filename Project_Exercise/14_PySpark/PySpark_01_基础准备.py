"""
演示获取pyspark的执行环境入库对象:SparkContext
并通过SparkContext对象获取当前pyspark的版本
"""

# 导包
from pyspark import SparkConf, SparkContext


# 创建SparkConf类对象  --链式调用的写法
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")  # 定义conf变量接收类对象,通过SparkConf()类构建类对象,并设置运行模式"local[*]",设置当前Spark任务程序名称"test_spark_app"
# 上面使用链式调用的写法等效以下传统写法:
# conf = SparkConf()
# conf.setMaster("local[*]")            --setMaster("local[*]")的返回值是SparkConf()
# conf.setAppName("test_spark_app")     --setAppName("test_spark_app")的返回值是SparkConf()

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)   # 构造SparkContext()实例化对象,传入参数:conf=conf对象,定义sc接收,即:执行环境入口对象.

# 打印PySpark的运行版本
print(sc.version)  # 通过打印sc对象的version属性来打印当前spark的版本


# 停止SparkContext对象的运行(停止PySpark)
sc.stop()  #


