"""
演示全国疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据文件
f = open("./疫情.txt", "r", encoding="UTF-8")  # 定义变量f接收open方法打开的文件内容
data = f.read()  # 定义data接收变量f用read方法读取到的全部数据

# 关闭文件
f.close()

# 取到各省数据
# 将字符串json转换为Python的字典
data_dict = json.loads(data)  # 定义data_dict基础数据字典接收来自使用json模块中loads方法将data数据转换成的Python字典
# 从字典中取出省份数据
province_data_list = data_dict["areaTree"][0]["children"]

# 组装每个省份和确诊人数为元组,并各个省份的数据都封装入列表内
data_list = []  # 绘图需要用的数据列表
for province_data in province_data_list:  # 使用for循环遍历province_data_list这个列表,并存入province_data中
    province_name = province_data["name"]  # 用变量province_name接收["name"],即省份名称
    province_confirm = province_data["total"]["confirm"]  # 用变量province_confirm接收["confirm"]的内容,即确诊人数
    data_list.append((province_name, province_confirm))  # 通过append方法将变量province_name和变量province_confirm封装成的元组添加到data_list列表中.
print(data_list)

# 创建地图对象
National_Outbreak_map = Map()

# 添加数据
National_Outbreak_map.add("各省份确诊人数", data_list, "china")

# 设置全局配置,定制分段的视觉映射
National_Outbreak_map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000以上", "color": "#990033"}
        ]
    )

)

# 绘图
National_Outbreak_map.render("全国疫情地图.html")


