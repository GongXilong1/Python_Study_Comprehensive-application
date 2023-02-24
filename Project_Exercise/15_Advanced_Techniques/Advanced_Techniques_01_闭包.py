"""
演示Python的闭包特性
"""


# 简单闭包
# def outer(logo):
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
#
# fn1 = outer("黑马程序员")  # fn1 的类型是一个函数
# fn1("大家好")  # 调用fn1,传入"大家好"这个参数
#
# fn2 = outer("传智教育")
# fn2("大家好 ")


# 使用nonlocal关键字修改外部函数的值
# def outer(num1):
#
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#
#     return inner
#
#
# fn = outer(10)  # 这个10是给num1的
# fn(10)  # 这个10是传给num2的.
# fn(10)

# num1对于inner来说是外部变量,num1对于outer来说是函数的内部变量.外界无法篡改num1


# 使用闭包实现ATM小案例
def account_create(initial_amount=0):

    def atm(num, deposit=True):  # deposit=True表示存款.
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款, +{num}, 账户余额, {initial_amount}")
        else:
            initial_amount -= num
            print(f"取款, -{num}, 账户余额, {initial_amount}")

    return atm


atm = account_create()  # 拿到atm函数对象

atm(100)  # 调用atm函数并传入100参数,即存100元
atm(200)
atm(100, deposit=False)  # deposit=False表示取款

# initial_amount=0是作用于account_create这个函数的变量,不是全局变量,不容易被篡改.








