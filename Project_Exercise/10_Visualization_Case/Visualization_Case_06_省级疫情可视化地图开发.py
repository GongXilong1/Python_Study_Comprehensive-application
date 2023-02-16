"""
演示河南省疫情地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取文件
f = open("./疫情.txt", "r", encoding="UTF-8")
data = f.read()

# 关闭文件
f.close()

# 获取河南省数据
# json数据转换为Python字典
data_dict = json.loads(data)

# 取到河南省数据
cities_data = data_dict["areaTree"][0]["children"][3]["children"]

# 准备数据为元组并放入list
city_data_list = []
for city_data in cities_data:
    city_name = city_data["name"]   # + "市"  疫情数据文件中地名后没有市的话,就在这句加上+ "市",这样才能和Map模块匹配.
    city_confirm = city_data["total"]["confirm"]
    city_data_list.append((city_name, city_confirm))
print(city_data_list)

# 手动添加济源市的数据
city_data_list.append(("济源市", 5))

# 构建地图
henan_map = Map()
henan_map.add("河南省疫情分布", city_data_list, "河南")

# 设置全局选项
henan_map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
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
    ),

)

# 绘图
henan_map.render("河南省疫情地图.html")



