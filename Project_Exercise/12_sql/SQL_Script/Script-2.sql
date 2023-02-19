--  DML学习

create table student(
	id int,
	name varchar(10),
	age int
);

--  数据插入演示
insert into student (id) values(1), (2), (3);

insert into student(id, name, age) values(4, '周晓晓', 20), (5, '林袁杰', 26);  -- 字符串字面量即周晓晓,在SQL使用中需要用单引号包起来.

insert into student values(6, '周大声', 27), (6, '张大有', 28); 


--  数据删除演示

delete from student where id = 4;  -- 删除student这个表中id=4对应的内容.

delete from student where id <= 5;  -- 删除student这个表中id<=5对应的内容.

delete from student where age = 27;   -- 删除student这个表中age = 27对应的内容.

delete from student;  -- 删除 student表中所有的内容,不写后面的where条件判断就是对全表的操作.


--  数据更新演示

update student set name = '王二哈' where id = 4;   -- 当id = 4的对应内容中更新成name = '王二哈'

update student set name = '喵新人';  --  把student表中name都更新成'喵新人',不写后面的where条件判断就是对全表的操作.




