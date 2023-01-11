# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#! D:\Program Files\Python3.10.2amd64\python.exe

"""-------------------------------------"""

import Cards_tools

while True:  # 无限循环，由用户主动决定什么时候退出循环！

    # 显示功能菜单
    Cards_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:

        # 新增名片处理
        if action_str == "1":
            Cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            Cards_tools.show_all()
        # 查询名片
        elif action_str == "3":
            Cards_tools.search_card()

        # pass  # 如果在开发程序时，不希望立刻编写分支内部的代码，可以使用 pass 关键字，表示一个占位符，能够保证程序的代码结构正确！，程序运行时，pass 关键字不会执行任何的操作！

    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break

        # pass
    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择")






