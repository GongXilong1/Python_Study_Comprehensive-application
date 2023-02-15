"""
演示JSON数据和Python字典的相互转换
"""
import json  # 导入json模块

# 准备列表,列表内每一个元素都是字典,将其转换为JSON
data = [{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 12}, {"name": "赵小虎", "age": 16}]  # 定义列表data的内容
json_str = json.dumps(data, ensure_ascii=False)  # 定义json_str变量接收使用json模块中dumps方法处理传入data这个列表参数后的结果,
# 以及处理传入ensure_ascii=False这个参数的结果. ensure_ascii=False  表示:不使用ASCII码转换内容.
# 不写ensure_ascii这个参数值默认为:ensure_ascii=Ture, 即:列表内的中文就会转换成Unicode字符.
print(type(json_str))  # 打印输出json_str的类型
print(json_str)  # 打印输出json_str的内容

# 准备字典,将字典转换为JSON
d = {"name": "周杰伦", "addr": "台北"}  # 定义字典d的内容
json_str = json.dumps(d, ensure_ascii=False)  # # 定义json_str变量接收使用json模块中dumps方法处理传入d这个字典参数后的结果
print(type(json_str))  # 打印输出json_str的类型
print(json_str)  # 打印输出json_str的内容

# 将JSON字符串转换为Python数据类型[{k:v,k:v}], {[k:v, k:v]}
s = '[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 12}, {"name": "赵小虎", "age": 16}]'  # 定义s这个json字符串
list1 = json.loads(s)  # 定义list1变量接收使用json模块中loads方法处理传入s这个json字符串参数后的结果
print(type(list1))
print(list1)

# 将JSON字符串转换为Python数据类型{k:v, k:,v}
s = '{"name": "周杰伦", "addr": "台北"}'  # 定义s这个json字符串
dict1 = json.loads(s)  # 定义dict1变量接收使用json模块中loads方法处理传入s这个json字符串参数后的结果
print(type(dict1))
print(dict1)
