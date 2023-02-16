"""
扩展列表的sort方法
在学习了将函数作为参数传递后,我们可以学习列表的sort方法来对列表进行自定义排序
"""

# 准备列表
my_list = [["a", 33], ["b", 55], ["c", 11]]


# # 排序,基于带名函数
# def choose_sort_key(element):
#     return element[1]  # 按照列表中每个元素的下标1排序,
#
#
# my_list.sort(key=choose_sort_key, reverse=True)  # key=用于接收函数,reverse为设置反转,默认是False,这个设置Ture为反转.
# print(my_list)

# 排序,基于lambda匿名函数
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)

