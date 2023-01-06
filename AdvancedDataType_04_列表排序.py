name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
num_list = [6, 8, 4, 1, 10]

# 升序
# name_list.sort()  # 按照字母顺序a-z去排列字符串
# num_list.sort()  # 按照数字0-10的增大顺序去排列

# 降序
# name_list.sort(reverse=True)  # reverse 使反转  默认情况下：reverse = False
# num_list.sort(reverse=True)
# num_list.sort()

# 逆序（反转）
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)


