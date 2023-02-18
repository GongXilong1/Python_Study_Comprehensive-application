"""
面向对象,数据分析案例,主业务逻辑代码
实现步骤:
1. 设计一个类,可以完成数据的封装
2. 设计一个抽象类,定义文件读取的相关功能,并且用子类实现具体功能
3. 读取文件,生产数据对象
4. 进行数据需求的逻辑计算(计算每一天的销售额)
5. 通过PyEcharts进行图形绘制
"""

from Data_Analysis_Case_file_define import TextFileReader, JsonFileReader
from Data_Analysis_Case_data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType


text_file_reader = TextFileReader("./2011年1月销售数据.txt")
json_file_reader = JsonFileReader("./2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()  # list[Record]类型注解
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并为一个list来存储
all_data: list[Record] = jan_data + feb_data

# 开始数据计算  ---需要再理解理解
data_dict = {}

for record in all_data:
    if record.date in data_dict.keys():  # 判断record.data是否在data_dict这个字典中的所有key中,
        # 当前日期已经有记录了,所以和老记录做累加即可
        data_dict[record.date] += record.money  # 通过data_dict[record.data]取到老的记录,通过+=(表示把老的值和新的相加再写回去)累加当前的money
    else:
        data_dict[record.date] = record.money  # 进入else说明是第一条,还没有记录被记录,即让data_dict[record.date] = record.money

print(data_dict)

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))  # 通过Bar这个类构建一个类对象bar,在InitOpts构造方法中传入ThemeType主题类型为LIGHT.

bar.add_xaxis(list(data_dict.keys()))  # 添加x轴的数据为data_dict这个字典的所有key(并转换成列表之后)
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))  # 添加y轴的数据为data_dict这个字典的所有值(并转换成列表之后的),并写上标签销售额
# label_opts=LabelOpts(is_show=False)表示不显示数值标签
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额柱状图.html")
