xiaoming_dict = {"name": "xiaoming",
                 "age": 18, }

# 1. 统计键值对数量
print(len(xiaoming_dict))

# 2. 合并字典
temp_dict = {"height": 1.75,
             "age": 20, }
# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对。
xiaoming_dict.update(temp_dict)

# 3. 清空字典
# xiaoming_dict.clear()

# 4. 复制字典
new_dict1 = xiaoming_dict.copy()


print(xiaoming_dict)
print(new_dict1)

