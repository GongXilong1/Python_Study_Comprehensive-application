"""
演示Python递归操作
需求: 通过递归,找出一个指定文件夹内的全部文件

思路: 写一个函数, 列出文件夹内的全部内容, 如果是文件就收集到 list
如果是文件夹, 就递归调用自己, 再次判断.

"""
import os


def test_os():
    """演示os模块的3个基本方法"""
    # print(os.listdir("D:/Users/Administrator/PycharmProjects/Project_Exercise/15_Advanced_Techniques/test"))
    print(os.listdir("./test"))
    # os.listdir方法是列出路径下目录里的内容.
    # print(os.path.isdir("D:/Users/Administrator/PycharmProjects/Project_Exercise/15_Advanced_Techniques/test/a"))
    # os.path.isdir方法是判断所给路径是否为文件夹,是文件夹返回Ture,不是返回False.
    # print(os.path.exists("D:/Users/Administrator/PycharmProjects/Project_Exercise/15_Advanced_Techniques/test"))
    # os.path.exists方法是判断路径是否存在.


def get_files_recursion_from_dir(path):
    """
    从指定的文件夹中使用递归的方式, 获取全部的文件列表

    :return:list, 包含全部的文件, 如果目录不存在或者无文件就返回一个空list
    """

    file_list = []  # 定义空list 等待收集文件
    if os.path.exists(path):
        for f1 in os.listdir(path):
            new_path = path + "/" + f1  # 得到一级目录下各个文件或文件的新路径
            if os.path.isdir(new_path):  # 判断各个新路径是否为文件夹
                # 进入到这里, 表明这个目录是文件夹
                file_list += get_files_recursion_from_dir(new_path)
                # 使用递归的方式, 再次循环判断  ,通过+= 将再次循环得到的file_list和之前的file_list合并.

            else:
                file_list.append(new_path)  # 某个新路径是文件就收集到file_list这个列表中.

    else:
        print(f"指定的目录{path}, 不存在")
        return []

    return file_list


if __name__ == '__main__':
    result = get_files_recursion_from_dir("D:/Users/Administrator/PycharmProjects/Project_Exercise/15_Advanced_Techniques/test")

    print(result)






