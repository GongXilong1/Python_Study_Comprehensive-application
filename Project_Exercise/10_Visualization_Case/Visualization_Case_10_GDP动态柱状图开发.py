"""
演示第三个图表:GDP动态柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据
f = open("./1960-2019全球GDP数据.csv", "r", encoding="GB2312")  # encoding="GB2312"可以显示中文
data_lines = f.readlines()  # 每一行都读取的方式去读

# 关闭文件
f.close()

# 删除第一条数据
data_lines.pop(0)
# 运行时此句报错:AttributeError: 'str' object has no attribute 'pop',原因是上面这句:data_lines = f.readlines()少了最后一个字母s.

# 将数据转换为字典存储,格式为:
# { 年份: [ [国家,gdp], [国家,gdp], ......], 年份: [[国家,gdp], [国家,gdp], ......], ......}
# { 1960: [ [中国, 1234], [美国, 1222], ......], 1961: [ [中国, 1357], [美国, 1345], ......], ......}

# 先定义一个字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])  # 调用split方法通过","逗号来切割第一个元素,下标0,通过int()来转换成数字   ---年份
    country = line.split(",")[1]  # ---国家
    gdp = float(line.split(",")[2])  # 将第三个元素的内容都转换成浮点型   ---GDP数据
    # 如何判断字典里面有没有指定的key?
    # 异常捕获的方式
    try:
        data_dict[year].append([country, gdp])  # 如果没有异常,会有year年份数据,出现异常year中没有数据,  调用append追加[country, gdp]列表
    except KeyError:  # 如果异常,创建空列表,再追加列表
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})  # 传入字典参数用来设置主题,为LIGHT蓝黄粉.

# 排序年份
sorted_year_list = sorted(data_dict.keys())  # 通过调用data_dict这个字典的keys方法来将所有key提取出来,再用sort的方法将所有key从小到大的年份排序,

# for循环每一年的数据,基于每一年的数据,创建每一年的bar对象
for year in sorted_year_list:  # for循环遍历出按year排序后的数据
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # data_dict这个字典在按照year排序后,再按照其内部列表中[1]位置的元素进行排序,使用关键字传参,key传参,reverse=True表示GDP高的在第一位.

    # 取出本年份前8名的国家
    year_data8 = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data8:  # 用for循环从year_data8遍历出国家名和gdp数据,存放到变量country_gdp中,
        x_data.append(country_gdp[0])  # x轴数据添加country_gdp这个列表变量中的0位置的元素,即国家名.
        y_data.append(country_gdp[1] / 100000000)  # x轴数据添加country_gdp这个列表变量中的1位置的元素,即gdp数值,数值除以一亿将单位换算成亿.

    # 构建柱状图对象    # 在for中,将每一年的bar对象添加到时间线中
    bar = Bar()
    x_data.reverse()  # x轴数据反转显示
    y_data.reverse()  # y轴数据反转显示
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))  # position="right"表示数值标签在右侧
    # 反转x轴和y轴
    bar.reversal_axis()  # 让柱状图从上下方向显示改变为左右方向显示.

    # 设置每一年图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8名GDP数据")   # 传入的参数是:title=f"{year}年全球前8名GDP数据",f表示字符串格式化.
    )

    timeline.add(bar, str(year))  # 时间线上添加bar对象显示的图表,并显示年份,str(year)表示转成字符串

# 设置时间线自动播放
timeline.add_schema(
    play_interval=500,  # 播放速度1000毫秒
    is_timeline_show=True,  # 是否显示时间线 是
    is_auto_play=True,  # 是否自动播放 是
    is_loop_play=False  # 是否循环播放 否
)

# 绘图
timeline.render("1960-2019全球GDP前8国家.html")

