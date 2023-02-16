"""
演示第三个图表:GDP动态柱状图开发
"""

# 读取数据
f = open("./1960-2019全球GDP数据.csv", "r", encoding="GB2312")  # encoding="GB2312"可以显示中文
data_lines = f.readline()  # 每一行都读取的方式去读

# 关闭文件
f.close()

# 删除第一条数据
data_lines.pop(0)

# 将数据转换为字典存储,格式为:
# { 年份: [ [国家,gdp], [国家,gdp], ......], 年份: [[国家,gdp], [国家,gdp], ......], ......}
# { 1960: [ [中国, 1234], [美国, 1222], ......], 1961: [ [中国, 1357], [美国, 1345], ......], ......}
# 先定义一个字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])   # 调用split方法通过","逗号来切割第一个元素,下标0,通过int()来转换成数字   ---年份
    country = line.split(",")[1]  # ---国家
    gdp = float(line.split(",")[2])  # 将第三个元素的内容都转换成浮点型   ---GDP数据
    # 如何判断字典里面有没有指定的key?
    # 异常捕获的方式
    try:
        data_dict[year].append([country, gdp])  # 如果没有异常,会有year年份数据,出现异常year中没有数据,  调用append追加[country, gdp]列表
    except KeyError:  # 如果异常,创建空列表,再追加列表
        data_dict[year] = []
        data_dict[year].append([country, gdp])

print(data_dict)
# 排序年份


# 创建时间线对象


# for循环每一年的数据,基于每一年的数据,创建每一年的bar对象
# 在for中,将每一年的bar对象添加到时间线中


# 设置时间线自动播放

# 绘图



