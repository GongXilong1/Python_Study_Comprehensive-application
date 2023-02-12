import requests
from lxml import etree  # 从lxml模块中导入etree  解析xpath表达式
import os  # 导入os模块   文件处理模块

# 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}

# 发送请求获取所有地址列表
list_url = 'https://yys.163.com/media/picture.html'  # 壁纸列表url
list_resp = requests.get(list_url, headers=headers)

# 获取所有壁纸地址:
e = etree.HTML(list_resp.text)
imgs1 = [url[:url.rindex('/')]+'/1920x1080.jpg' for url in e.xpath('//div[@class="tab-cont"][1]/div/div/img/@data-src')]  # [1]表示获取横屏壁纸
imgs2 = [url[:url.rindex('/')]+'/1920x1080.jpg' for url in e.xpath('//div[@class="tab-cont"][2]/div/div/img/@data-src')]  # [2]表示获取竖屏壁纸


# print(imgs1)

# 保存所有壁纸
if not os.path.exists('heng'):
    os.makedirs('heng')
if not os.path.exists('shu'):
    os.makedirs('shu')

for url in imgs1:
    resp = requests.get(url, headers=headers)
    # print(url)
    # print(url.rindex('picture'))
    file_name = url[url.rindex('picture'):url.rindex('/')].replace('/', '_')+'.jpg'
    print('正在保存:'+file_name+'壁纸')

    with open(f'heng/{file_name}', 'wb') as f:
        f.write(resp.content)


# 下载单张的代码

# # 发送请求
# resp = requests.get(, headers=headers)
# print(resp.content)
#
# # 保存
# with open('a.jpg', 'wb') as f:  # 定义f方法
#     f.write(resp.content)
#


