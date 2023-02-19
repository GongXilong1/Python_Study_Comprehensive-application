--  库的操作

-- show databases; -- 单行注释
# 单行注释

/*
 * 
 * 多行注释
 * */


use sakila;  -- 使用库
select database();  -- 查看当前使用的数据库

create database test charset utf8;  -- 创建库 名称test 编码:utf8
show databases;  -- 展示所有库

drop database test; -- 删除库

