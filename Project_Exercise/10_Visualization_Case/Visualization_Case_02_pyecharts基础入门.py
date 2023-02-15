"""
演示pyecharts的基础入门
"""
# 导包
import pyecharts
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建一个折线图对象
line = Line()

# 给折线图对象添加x轴的数据
line.add_xaxis(["中国", "美国", "英国"])

# 给折线图对象添加y轴的数据
line.add_yaxis("GDP", [30, 20, 10])

# 通过render方法,将代码生成图像
line.render()

# 设置全局配置项,通过set_global_opts这个方法来设置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),  # 展示标题 ,,关键字传参,   pos_left表示位置靠左为居中,pos_bottom表示位置距离底部1%.
    legend_opts=LegendOpts(is_show=True),  # 展示图例
    toolbox_opts=ToolboxOpts(is_show=True),  # 展示工具箱
    visualmap_opts=VisualMapOpts(is_show=True)  # 展示视觉映射
)

# 通过render方法,将代码生成图像
line.render()
