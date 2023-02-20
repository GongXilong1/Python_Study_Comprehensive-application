--  DQL 分组聚合查询

select gender, avg(age), sum(age), min(age), max(age), count(*)  from newstu group by gender;   # 通过性别进行分组,然后再分别求出平均年龄.... 
  
-- 注意事项:group by中出现哪个列,哪个列才能出现在select中的非聚合中.          聚合函数:avg(age), sum(age), min(age), max(age), count(*)


