"""
演示 Python正则表达式 re模块的3个基础匹配方法
"""
import re

s = "1python jason python"

# match--从头匹配,匹配到一个为止,之后的就不匹配了.
result1 = re.match("python", s)
print(result1)
# print(result.span())
# print(result.group())

# search--搜索匹配,全局匹配,匹配到一个为止,之后的就不匹配了.
result2 = re.search("python", s)
print(result2)

# findall--搜索全部,匹配全部命中项.
result3 = re.findall("python", s)
print(result3)

