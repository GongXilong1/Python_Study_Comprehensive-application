--  作业练习

create table newstu(
	id int,
	name varchar(10),
	age int,
	gender varchar(10)

); 

insert into newstu (id, name, age, gender) values(10001, '周杰轮', 31, '男'), (10002, '王力红', 33, '男');

insert into newstu (id, name, age, gender) values(10003, '蔡依林', 35, '女'), (10004, '林志玲', 36, '女'), (10005, '刘德画', 35, '男'), (10006, '张大山', 31, '男'), (10007, '刘志龙', 15, '男'), (10008, '王晓晓', 31, '女'), (10009, '张一梅', 32, '女'), (10010, '王一茜', 25, '女'), (10012, '张晓红', 21, '女');

insert into newstu (id, name, age, gender) values(10013, '李大晓', 15, '男'), (10014, '吕甜甜', 36, '女'), (10015, '曾悦悦', 31, '女'), (10016, '刘佳慧', 21, '女'), (10017, '项羽凡', 23, '男'),(10018, '刘德强', 26, '男'),(10019, '王强强', 11, '男'),(10020, '林志慧', 25, '女');

insert into newstu (id, name, age, gender) values(10011, '陈一讯', 31, '男');


update newstu set name = '王力鸿' where id = 10002;

update newstu set name = '蔡依琳' where id = 10003;

update newstu set name = '林志灵' where id = 10004;

update newstu set name = '刘德滑' where id = 10005;   --  多人都要按照id修改name,可以合成到一句写吗?怎么写?

update newstu set age = 10 where id = 10006;   --  在同一个id下的,需要同时修改name和age怎么合成起来写?

update newstu set age = 11 where id = 10007;

update newstu set age = 33 where id = 10008;

update newstu set name= '王潇潇' where id = 10008;

update newstu set age = 20 where id = 10009;

update newstu set age = 13 where id = 10010;

update newstu set name= '王一倩' where id = 10010;

update newstu set name= '张晓光' where id = 10012;

update newstu set age = 33 where id = 10012;

update newstu set name= '陈一迅' where id = 10011;

update newstu set age = 33 where id = 10005;

update newstu set gender = '男' where id = 10012;




