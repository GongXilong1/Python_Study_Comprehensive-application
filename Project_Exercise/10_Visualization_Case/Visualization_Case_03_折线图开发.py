"""
演示可视化需求1: 折线图开发
"""
import json  # 导入json包
from pyecharts.charts import Line  # 从pyecharts.charts模块导入Line功能
from pyecharts.options import TitleOpts, LabelOpts  # 从pyecharts.options模块导入TitleOpts功能和LabelOpts功能

# 处理数据-美国 日本 印度
f_us = open("./折线图数据/美国.txt", "r", encoding="UTF-8")  # 定义变量f_us接收open方法打开后的内容,打开要处理的文件的目录,用r模式读取,编码方式UTF-8.
us_data = f_us.read()  # 定义变量us_data接收f_us变量用read方法读取后的结果.

f_jp = open("./折线图数据/日本.txt", "r", encoding="UTF-8")  # 定义变量f_jp接收open方法打开后的内容,打开要处理的文件的目录,用r模式读取,编码方式UTF-8.
jp_data = f_jp.read()  # 定义变量jp_data接收f_jp变量用read方法读取后的结果.

f_in = open("./折线图数据/印度.txt", "r", encoding="UTF-8")  # 定义变量f_in接收open方法打开后的内容,打开要处理的文件的目录,用r模式读取,编码方式UTF-8.
in_data = f_in.read()  # 定义变量in_data接收f_in变量用read方法读取后的结果.

# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")  # 将us_data头部内容删除后再赋值给us_data
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")  # 将jp_data头部内容删除后再赋值给jp_data
in_data = in_data.replace("jsonp_1629350745930_63180(", "")  # 将in_data头部内容删除后再赋值给in_data

# 去掉不合JSON规范的结尾
us_data = us_data[:-2]  # 去掉0到-2的内容,即:倒数第一个和倒数第二个字符的内容
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# JSON转Python字典
us_dict = json.loads(us_data)  # 定义us_dict接收通过json模块loads方法将us_data转换后的字典内容
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend key
us_trend_data = us_dict['data'][0]['trend']  # 定义us_trend_data接收us_dict取到trend的key
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据,用于x轴,取2020年的,即美国序号0-314的 日本0-314的 印度0-268的
us_x_data = us_trend_data['updateDate'][:314]  # 通过取us_trend_data中updateDate这个key的值作为x轴数据,只取0-314的,定义变量us_x_data接收.
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:268]
print(us_x_data)

# 获取确诊数据,用于y轴,取2020年的,即序号0-314的 日本0-314的 印度0-268的
us_y_data = us_trend_data['list'][0]['data'][:314]  # 通过取us_trend_data中data这个key的值作为y轴的数据,只取0-314的,定义变量us_y_data接收.
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:268]
print(us_y_data)

# 生成图表
line = Line()  # 构建Line对象,命名line..   没加Line后的()导致如下报错

    # Traceback (most recent call last):
    #   File "D:\Users\Administrator\PycharmProjects\Project_Exercise\10_Visualization_Case\Visualization_Case_03_折线图开发.py", line 53, in <module>
    #     line.add_xaxis(us_x_data)  # x轴可以共用,使用一条即可.
    # TypeError: RectChart.add_xaxis() missing 1 required positional argument: 'xaxis_data'

# 添加x轴数据
line.add_xaxis(us_x_data)  # x轴可以共用,使用一条即可.

# 添加y轴数据
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))  # 添加m国的y轴数据   LabelOpts控制曲线上的数字标签是否显示
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))  # 添加日本的y轴数据
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))  # 添加印度的y轴数据

# 设置全局选项
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")  # pos_left表示位置水平为居中,pos_bottom表示位置距离底部1%.
)


# 调用render方法,生成图表
line.render()

# 关闭文件对象
f_us.close()
f_jp.close()
f_in.close()


