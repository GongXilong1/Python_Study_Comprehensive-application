hello_str = "hello world"

# 1. 判断是否以指定字符串开始
print(hello_str.startswith("Hello"))  # 在程序世界中，小写字母和大写字母是完全不同的两个字符

# 2. 判断是否以指定的字符串结束
print(hello_str.endswith("world"))

# 3. 查找指定字符串
# index方法同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find("llo"))

# 使用index方法时，如果指定的字符串不存在，程序会报错。
# 使用find方法时，如果指定的字符串不存在，会返回-1。
print(hello_str.find("abc"))

# 4. 替换字符串
#  replace 方法执行完成之后，会返回一个新的字符串，注意：不会修改原有字符串的内容，。
print(hello_str.replace("world", "python"))

print(hello_str)



