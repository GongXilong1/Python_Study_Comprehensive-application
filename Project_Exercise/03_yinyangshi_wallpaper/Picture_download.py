import requests
from lxml import etree

# 图片地址:
url = 'http://www.netbian.com/meinv/'

# 伪装
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}

# 发送请求
resp = requests.get(url, headers=headers)
resp.encoding = 'gbk'  # 告诉软件用中文显示

print(resp.text)

# 解析
xp = etree.HTML(resp.text)

# 提取图片地址
img_urls = xp.xpath('//ul/li/a/img/@src')
img_names = xp.xpath('//ul/li/a/img/@alt')

# 保存
for u, n in zip(img_urls, img_names):
    print(f'正在下载: 图片名: {n}')
    img_resp = requests.get(u, headers)

    with open(f'./Picture_download/{n}.jpg', 'wb') as f:
        f.write(img_resp.content)

