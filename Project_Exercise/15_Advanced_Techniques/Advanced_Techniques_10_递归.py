"""
演示Python递归操作
需求: 通过递归,找出一个指定文件夹内的全部文件

思路: 写一个函数, 列出文件夹内的全部内容, 如果是文件就收集到 list
如果是文件夹, 就递归调用自己, 再次判断.

"""
import os


def test_os():
    """演示os模块的3个基本方法"""
    print(os.listdir("D:/Users/Administrator/PycharmProjects/Project_Exercise/15_Advanced_Techniques/test"))
    print(os.path.isdir("D:/Users/Administrator/PycharmProjects/Project_Exercise/15_Advanced_Techniques/test/a"))
    print(os.path.exists("D:/Users/Administrator/PycharmProjects/Project_Exercise/15_Advanced_Techniques/test"))










