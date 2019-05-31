RDBMS(relational database management system)关系型数据库，包括mysql，oracle
mysql图形界面：navicat（解压后删除.navicat64，取消安装wine）
数据类型：INT，CHAR（max_char_number),一般用VARCHAR（动态大小），TEXT（0-65535字节），decimal（5， 2）共存5位数，2位小数
约束：主键（primary key），外键（foreign key），非空（not null）， 唯一（unique，此字段的值不允许重复），默认（default）
外键约束会减慢修改的速度。为保证有消息，可以在**逻辑层**进行控制。

登陆: mysql -uroot -pmysql

显示已有数据库： show databases;  // 以；结束命令输入
查看语句，使用show： show create database base_name charset=utf8;
显示时间，版本： select now(); select version();  // 使用select选择函数来显示，而非show

1.
注释： -- 注释内容
创建数据库： create database base_name charset=utf8; // charset默认为latin
删除数据库： drop database base_name  // 若数据库名带-，则需输入\`base-name\`。
使用数据库： use base_name
显示当前使用中的数据库名称： select database();  // 需先用use使用数据库。

2.
显示当前数据库的所有数据表： show tables;
创建数据表: create table table_name(字段 类型 约束[, 字段 类型 约束]);  // int unsigned
删除数据表： drop table table_name
查看表格本身（而非表中数据）的结构： desc table_name;  // desc是describe的缩写？

3.修改表格结构（alter）
增加字段： alter table table_name add 字段名 类型即约束；
修改字段： alter table table_name modifiy 字段名 类型即约束；
修改已有字段为新字段： alter table table_name change 原字段 新字段名 类型即约束；
删除字段： alter table table_name drop 字段名 类型即约束；  // 会将数据一并删除


4.数据修改（curd：create,update,retrive,delete)
显示整个表格的数据： select \* from table_name [where 字段=值];  //条件也可以是字段>值
插入数据： insert into table_name [(要插入数据的字段)] values(具体数值）[,(具体数值)];
修改某一字段的数据： update students set 字段=值[,字段=值] where id=5;
删除数据： delete from table_name where 字段=值;  // 没有where就会删除所有数据

对于一个用户一般只标记已经删除而非真正删除。
alter table table_name add user_deleted bit default 0;
update table_name set user_deleted=1 where user_id=13; // 1表示账户已无效。

5.数据查询
select [distinct] 别名.字段[,别名.字段] from table_name as 别名；  // distinct去重

where 条件1 and 条件2;
where not (条件1 and 条件2);
1. 条件查询： 
* where 字段=值  -- 表示精确查询
* where 字段 like 值%  -- 表示模糊查询，%替换1或多个，_替换1个。
* where 字段 rlike 值%  -- 表示正则查询

2. 范围查询
where 字段 not in (值1， 值2， 值3）；
where [not] (字段 [not] between int1 and 值2);  // not可前可后，括号内为1个条件整体
where 字段 is null；

6.对查询到的数据排序，在最后加上order
order by 字段 asc/desc [,字段 asc/desc];  //先判断前边的条件（ascend，descend）

7.聚合函数(求和、求数量、求平均值等）、分组
select count(*) from table_name where 条件；  // count计算数据条数
select round(sum(字段)/count(*), 2) from table_name where 条件；
此时显示结果为1个值

select **gender**, sum(age)/group_concat(name, " ", age)[,avg(age)] from table_name where 条件 group by **gender** having avg（age) > 20;  -- group字段为gender，所以前边的字段也要为gender
1. 先用where确定所选内容，
2. 使用group按字段中不同的值来分组。
3. 使用having仅显示符合筛选条件的组。
4. 对不同的组都1.求出值，或2.使用group_concat()显示组中的每条数据的字段内容。

7.分页
最后加上 limit 每页显示数量；
或者 limit 开始项， 每页显示数量； --开始项从0开始，放在order后边。


