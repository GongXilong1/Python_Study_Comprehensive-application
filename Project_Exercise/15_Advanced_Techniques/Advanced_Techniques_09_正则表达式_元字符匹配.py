"""
演示Python 正则表达式使用元字符进行匹配
"""
import re

# s = "jason1 @@python2 !!666 ##jsaon3"
#
# # \d 匹配数字
# result1 = re.findall(r'\d', s)  # NOTE 字符串前面带上r的标记,表示字符串中转义字符无效,就是普通字符的意思.
# print(result1)  # 运行结果: ['1', '2', '6', '6', '6', '3']
#
# # \W 匹配特殊字符,即非单词字符
# result2 = re.findall(r'\W', s)  # W一定要大写.
# print(result2)  # 运行结果: [' ', '@', '@', ' ', '!', '!', ' ', '#', '#']
#
# # 匹配所有单词字母和数字
# result3 = re.findall(r'[a-zA-Z0-9]', s)
# # result3 = re.findall(r'\w', s)
# print(result3)  # 运行结果: ['j', 'a', 's', 'o', 'n', '1', 'p', 'y', 't', 'h', 'o', 'n', '2', '6', '6', '6', 'j', 's', 'a', 'o', 'n', '3']
#
# # 匹配数字5-7的
# result4 = re.findall(r'[5-7]', s)
# print(result4)  # 运行结果: ['6', '6', '6']


# 匹配账号,只能有字母和数字组成, 长度限制6-10位
r1 = '^[0-9a-zA-Z]{6,10}$'  # ^表示匹配字符串开头,$表示匹配结尾,[0-9a-zA-Z]表示所有数字和大小写的字母,{6,10}表示限制长度在6-10位,6和10之间一定不能有空格,这是正则表达式的规范.
s1 = '123456aA'
result5 = re.findall(r1, s1)  # findall(r, s)表示规则是r,被匹配的是s.
print(result5)


# 匹配QQ号,要求纯数字, 长度5-11位,第一位不能为0.
r2 = '^[1-9][0-9]{4,10}$'  # [1-9]表示第一位不能为0,[0-9]表示纯数字,{4-10}第一位已经判断过了,所以长度限制是{4,10}.
s2 = '12345678'
result6 = re.findall(r2, s2)
print(result6)


# 匹配邮箱地址, 只允许qq 163 gmail 这三种邮箱地址
# {内容}.{内容}@{内容}.{内容}.{内容}
# 示例: abc.efg.daw@qq.com
r3 = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
# [\w-]表示匹配示例中abc部分, (\.[\w-]+)表示匹配示例中abc部分.efg.daw部分,
# *星号表示.efg.daw部分可以出现0次或无数次, (qq|163|gmail)中的竖线|表示匹配三个域名中的任意一个,
# 示例中.com部分也同样可以用(\.[\w-]+)去匹配, 最后的+加号表示.com这个部分至少要出现一次.
s3 = 'a.b.c.d.e.f.g@163.com.a.z.c.d.e'
s4 = 'a.b.c.d.e.f.g@126.com.a.z.c.d.e'
result7 = re.findall(r3, s3)
result8 = re.match(r3, s3)
result9 = re.match(r3, s4)
# NOTE findall方法特点: 如果规则中有括号进行分组,findall处理后会按照括号分组匹配返回结果,不是整体匹配返回结果.如果需要整体匹配,那么就给正则表达式整体加个括号.
print(result7)
print(result8)
print(result9)

