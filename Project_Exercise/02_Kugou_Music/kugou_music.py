import requests  # 导入发送请求模块

# 音乐地址:
m_url = 'https://webfs.ali.kugou.com/202302112209/aca1f0ee6cf33df21f52a31bb26769ad/part/0/960111/KGTX/CLTX001/clip_bfbdd3df47727b701d4480ea36a8f73b.mp3'

# 伪装
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# 发送请求
m_resp = requests.get(m_url, headers=headers)  # 定义变量m_resp接收requests模块中get方法的返回值.


# 服务器回应数据--保存数据
with open('dayu.mp3', 'wb') as f:  # 命名目标文件名dayu.mp3  w是write,b是byte,
    f.write(m_resp.content)








