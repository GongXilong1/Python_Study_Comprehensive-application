--  DQL  排序分页查询


select * from newstu where age > 20 order by age asc;    -- order by age表示按照age排序, asc表示从小到大显示,不写asc的话,通常系统默认也是升序排列显示.
select * from newstu where age > 20 order by age desc;   -- desc表示从大到小排序显示,



select * from newstu limit 5;  -- 查询只显示5条.

select * from newstu limit 10, 5;  --  查询显示从第10条之后显示5条.即取第11条到第15条的数据.

select age , count(*)  from newstu where age >20 group by age order by age limit 3;   --  查询在各个年龄段都有多少人.并按照年龄排序,最后只显示前三条.

--  select \  from \where \group by \ order by \limit  这些关键字都要按照这个前后顺序去写.

 
/*  
 * 注意事项:
 * where \group by \ order by \limit 这些关键字按照实际需求去写,没有可省略
 * select和from是必须写的.
 * 执行顺序:from -> where -> group by和聚合函数 -> select -> order by -> limit
 * 
 */

 