import os
import PIL
from PIL import Image

# 打开文件
im = Image.open('./Picture_download/古力娜扎 包臀裙 美腿 绿色背景 苹果 美女壁纸.jpg')
w, h = im.size  # 定义变量w h 接收图片大小

# 合成的行数 列数:
image_row = 4  # 行数
image_column = 3  # 列

# for循环遍历文件名
# for n in os.listdir('./Picture_download'):

# 保存所有名字
names = os.listdir('./Picture_download')

# 合成
new_img = Image.new('RGB', (image_column * w, image_row * h))  # 定义新画布   列乘以宽   行乘以高
for y in range(image_row):  # y是行的遍历结果 =0 1 2 3
    for x in range(image_column):  # x是列的遍历结果  x = 0 1 2
        # 打开要合成的图片
        o_img = Image.open('./Picture_download' + names[image_column * y + x])
        new_img.paste(o_img, (x * w, y * h))
new_img.save('new_img1')
