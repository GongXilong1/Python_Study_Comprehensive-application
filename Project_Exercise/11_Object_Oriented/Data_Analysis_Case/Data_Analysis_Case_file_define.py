"""
与文件相关的类定义
"""
import json

from Data_Analysis_Case_data_define import Record


# 先定义一个抽象类用来做顶层设计,确定有哪些功能需要实现
class FileReader:

    def read_data(self) -> list[Record]:  # 返回值的注解用->符号后加上要返回的类型list,用[]记录内部存储的是Record对象,
        """读取文件的数据,读到的每一条数据都转换为Record对象,将它们都封装到list内返回即可"""
        pass  # 因为是抽象方法,可以用pass占位.


class TextFileReader(FileReader):  # 定义TextFileReader文本文件读取类,并继承FileReader类

    def __init__(self, path):
        self.path = path        # 定义成员变量记录文件的路径

    # 复写(实现抽象方法)父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")  # 在方法内部使用成员变量要记得前面有self.   定义文件对象f接收读取的数据

        record_list: list[Record] = []  # 使用: list[Record]这个类型注解表示record_list里面存放的是Record的类对象.
        for line in f.readlines():  # 通过for循环f.readlines方法逐行读取的内容后拿到文件的行.
            line = line.strip()  # line里默认有回车换行符,使用strip方法将回车换行符去掉.--即消除读取到的每一行数据中的\n
            data_list = line.split(",")  # 使用split方法将数据中的","去掉,定义data_list接收去掉","的列表数据.
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            # 定义record对象接收Record类对象传入四个数据(data_list列表中四个元素对应的内容)后的结果,--int(data_list[2])表示将字符串转换成数字.
            record_list.append(record)  # 将record对象添加到record_list列表中

        f.close()  # f文件用完后进行关闭操作
        return record_list  # 返回到record_list


class JsonFileReader(FileReader):  # 定义JsonFileReader json文件读取类,并继承FileReader类

    def __init__(self, path):
        self.path = path        # 定义成员变量记录文件的路径

    # 复写(实现抽象方法)父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")  # 在方法内部使用成员变量要记得前面有self.   定义文件对象f接收读取的数据

        record_list: list[Record] = []  # 使用: list[Record]这个类型注解表示record_list里面存放的是Record的类对象.
        for line in f.readlines():  # 通过for循环f.readlines方法逐行读取的内容后拿到文件的行.
            data_dict = json.loads(line)  # 定义data_dict字典接收使用json模块中的loads方法将line字符串转换成Python的内部数据格式数据,
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])  #  构建record对象,传入data_dict["date"]等参数
            record_list.append(record)

        f.close()  # f文件用完后进行关闭操作
        return record_list  # 返回到record_list


if __name__ == '__main__':  # 使用此句,保证此页代码可以顺利运行,在导包的时候此句里的代码不会被执行.
    text_file_reader = TextFileReader("./2011年1月销售数据.txt")  # 构建text_file_reader这个类对象,并传入path文件路径参数
    json_file_reader = JsonFileReader("./2011年2月销售数据JSON.txt")  # 构建json_file_reader这个类对象
    list1 = text_file_reader.read_data()  # text_file_reader类对象调用read_data方法.
    list2 = json_file_reader.read_data()  # json_file_reader类对象调用read_data方法.

    for l in list1:
        print(l)

    for l in list2:
        print(l)

