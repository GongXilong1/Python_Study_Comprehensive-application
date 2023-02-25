"""
演示设计模式值工厂模式
"""


class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class PersonFactor:  # 创建工厂类
    def get_person(self, p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacher()


pf = PersonFactor()
worker_zhang = pf.get_person('w')
stu_wang = pf.get_person('s')
teacher_li = pf.get_person('t')



