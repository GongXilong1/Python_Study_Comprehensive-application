-- 表的操作

use world;
show tables;  -- 查看所有表

create table student(   -- 创建表,名称student.
	id int,  -- id列,类型int整数.
	name varchar(255),  -- name列,类型varchar,即字符串,最大长度限制为255.
	age int  -- age列 类型int整数. float为浮点数,,,timestamp为时间戳类型.
);

drop table student;  --  删除表 


