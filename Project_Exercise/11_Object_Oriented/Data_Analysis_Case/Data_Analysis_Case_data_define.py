"""
数据定义的类
"""


class Record:

    def __init__(self, data, order_id, money, province):  # 定义构造方法,并接收参数data, order_id, money, province
        self.date = data  # 将参数data赋值给成员变量self.date,-----在方法中使用成员变量,要在变量前加关键字self.
        self.order_id = order_id  # 订单ID
        self.money = money  # 订单金额
        self.province = province  # 销售省份

    def __str__(self):  # 通过__str__(self):方法,改变它输出行为
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"  # 输出四个成员变量的信息


