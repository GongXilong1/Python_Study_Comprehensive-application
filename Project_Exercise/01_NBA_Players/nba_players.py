import requests
from lxml import etree  # 从lxml模块导入etree


# 发送地址
url = 'https://nba.hupu.com/stats/players'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}  # 伪装成浏览器去访问


# 发送请求

resp = requests.get(url, headers=headers)  # 定义resq变量接收响应
print(resp.text)

# 处理结果

# 解析响应的数据

# 是否保存



