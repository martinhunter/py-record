## 关系型数据库, 基于关系模型
> RDBMS(relational database management system)
> 关系型数据库，包括mysql，oracle. [关系型数据库的起源](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf)

理论基础:集合论(set theory)

原理： 每张表是一个集合，通合之间存在关系（如交集）

#### [key](https://www.studytonight.com/dbms/database-key.php)

作用：每个key都是唯一的，如此可快速找到一条唯一记录，如此可仅对此此记录修改。

* 主键（primary key） 性质：非空（not null）， 唯一（unique，此字段的值不允许重复），默认（default）
* 外键（foreign key）与引用表相关联（此外键是引用表的主键）。不同主键可对应同一外键，但反过来不行。
* 外键的作用：设定了可选值的集合，表格的外键仅可从此集合中获取值（除非为空值），而不能随意设置值

* 候选键（candidate key，又可称为候选主键）: 1个或多个非主键的组合，能与主键一样定位一条唯一的记录，且使用最少的属性（无冗余）
* 超键（super key）：1个或多个非主键的组合，能与主键一样定位一条唯一的记录，超键就是这些组合的集合
* [复合键（composite key）](https://beginnersbook.com/2015/04/keys-in-dbms/)：2个或多个键组合生成一个唯一结果，能与主键一样定位一条唯一的记录。符合此条件的主键、超键、候选键都可称复合键

* 每一列又可称为一个属性（attribute）
* 主键属性：是候选键的一部分
* 非主键属性：非候选键

* 外键约束会减慢修改的速度。为保证有消息，可以在**逻辑层**进行控制。

### 描述表的关系

一对一：2个表主键相同（主键和外键是同一个），其他列都不同，通常用于隔离机密信息，分隔后可加快查询，或避免空值插入

一对多：普通表将引用表作为外键，引用表为一，普通表为多

多对多：是前2者的集合。先创建一个中间表。中间表创建2个外键，引用2张表。

### 规范化
起因：一个表格中过多列，冗余，导致插入更新删除行都操作困难。
常用解决方法：将一个表拆分为多个表

NOTE：规范化不是消除冗余，而是减少冗余。



### 每个范式（normal form）都先要满足前一个范式

- 第一范式
    - 列仅包含原子值（不能再细分），作者列的一个单元格不能放多个作者
    - 1列的数据类型相同
    - 列名不重复
    - 没有重复的组（2个或多个逻辑相关联的列的集合），例如一本书有多个作者，不应创建多个作者列，因为作者是逻辑相关联的，只应创建一个
    - solve：简单方法在现有表中将1本书的多作者分成多列，复制多次书信息（其他行的）,但是违反了第二范式
    - solve2: 也可将author放入新的字表，创建多对多的关系
- 第二范式
    - 不是部分依赖的，而是完全依赖。`A->B`表示B依赖于A,`{A,B}->C`表示C依赖于AB复合键
        - 依赖性/函数依赖（dependency/function dependency）：表格的所有其他列都通过主键获得,主键外的列并不能推得另外列的值
        - 完全依赖：列完全依赖了主键（候选键），而非部分
        - 部分依赖：列只依赖了主键（候选键）的一部分，而非其全部
        - exp：1个表有2个外键，外键组成的候选键能更好地描述和查找，候选键也等同于一个主键。
        - 表中的一些列可能只依赖于其中一个外键（即只知道其中一个外键就确定此列的值），此时这些列就是部分依赖。
        - solve: 部分依赖的列移出，用依赖的外键和这些列创建1对1表。或将部分依赖的列改为外键，依然创建新表
    - 作用：更加清晰
- 第三范式
    - 不能传递依赖（transitive dependency）
        - 依赖传递：A->B,但A,B都不是主键属性，但prime->A，因此称为传递依赖
        - solve1: A是超键
        - solve2: B是主键属性,但是违反Boyce-Codd范式
        - solve problem: 将此非主键列及依赖的非主键移出并创建新表，创建ID作为主键
    -作用：减少数据复制
- 更高级的范式：关系模型不需要，但会用来避免冗余的高级范式
- Boyce-Codd范式（又称3.5范式，是第三范式的拓展）
    - 候选键列的一部分不能依赖于非主键列
    - solve: A是主键属性，B->A，则B必须是超键
- 第四范式
    - 不能多值依赖（Multi-valued Dependency）
        - 多值依赖出现的条件：
        - A->B,单一A值对应多个B值,可能就会有多值依赖
        - 至少有3列
- 第五范式
    - 没有连接依赖（join Dependency）
        - 连接依赖：将表格拆分，然后重组，依然能得到原表格，而信息不丢失
        - 没有连接依赖的表格，拆分重组后，会信息丢失或创建新条目
    - 没有连接依赖的表格说明已经到达最小的程度，已不可再分。
    - 但不是所有的表格都要达到没有连接依赖的程度。

### exp: 一个有范式问题的表格

book_id(primary key) | publisher | title | author | pub_date |
--- | --- | --- | --- | --- |
OSN21329 | Oraley | insight | Mark,Twin | 1947-4-7
OSN21132 | Oraley | outsight | Mark,Town | 1952-4-15
OSN21343 | BkTown | brief tour | Bill,Twin | 1947-4-24
OSN21124 | Oraley | Great town | Mark,Alan,Willy | 1953-5-27

#### after 1st normal form.

> {title,author}组成候选键定位一条记录，但其他列与author无关，违反第二范式

book_id | publisher | title | author | pub_date |
--- | --- | --- | --- | --- |
OSN21329 | Oraley | insight | Mark | 1947-4-7
OSN21329 | Oraley | insight | Twin | 1947-4-7
OSN21132 | Oraley | outsight | Mark | 1952-4-15
OSN21132 | Oraley | outsight | Town | 1952-4-15
OSN21343 | BkTown | brief tour | Bill | 1947-4-24
OSN21343 | BkTown | brief tour | Twin | 1947-4-24
OSN21124 | Oraley | Great town | Mark | 1953-5-27
OSN21124 | Oraley | Great town | Alan | 1953-5-27
OSN21124 | Oraley | Great town | Willy | 1953-5-27

#### after 2nd normal form，并增加一列出版社排行

> pub_rank不是主键，且只依赖publisher（非主键，依赖于主键），与主键/候选键无关，违反了第三范式

book_id(primary key) | publisher | title | pub_date | pub_rank | 
--- | --- | --- | --- | --- |
OSN21329 | Oraley | insight | 1947-4-7 | 1
OSN21132 | Oraley | outsight | 1952-4-15 | 1
OSN21343 | BkTown | brief tour | 1947-4-24 | 4
OSN21124 | Oraley | Great town | 1953-5-27 | 1
OSN21117 | Meeter | bulid palace | 1923-4-21 | 2

title | author_id |
--- | --- |
OSN21329 | 1
OSN21329 | 2
OSN21132 | 1
OSN21132 | 3
OSN21343 | 2
OSN21343 | 4
OSN21124 | 1
OSN21124 | 5
OSN21124 | 6

> 可为作者设置id，以避免重名问题

author_id(primary key) | author | Age | contry |
--- | --- | --- | --- |
1 | Mark | 26 | Ame
2 | Twin | 32 | Bri
3 | Town | 31 | France
4 | Bill | 24 | Ame
5 | Alan | 37 | Japan
6 | Willy | 42 | Germany

#### after 3rd normal form

> 将pub_rank列移出，并创建publisher表

publisher | pub_rank |
--- | --- |
Oraley | 1
Meeter | 2
BkTown | 4

#### before 4th normal form

> name->address，hobby和course则多值依赖于name，且hobby与course互相独立

name | address | hobby | course |
--- | --- | --- | --- |
Mar | Wall Street | piano | French
Mar | Wall Street | piano | Chemistry
Mar | Wall Street | baseball | French
Mar | Wall Street | baseball | Chemistry
Mar | Wall Street | reading | French
Mar | Wall Street | reading | Chemistry

solve: 以name为主键分为3张表

#### a table qualified for 5th normal form

> 由于两两相关，必须要拆分成3张表才可,
但3张表再次组合却不会得到原来的表，而会多出许多（不在原表内的）信息。
因此此表符合第五范式

supplier | product | customer |
--- | --- | --- |
KFC | chicken | Malin
McNaldo | chicken | Pielo
KFC | french fries | Pielo
McNaldo | french fries | Nindo
KFC | coffee | Pielo
McNaldo | coffee | Shroud
Walles | coffee | Nindo

### exp: 使用->表示范式问题

preset: {A,B}组成候选键,C,D不是主键属性。`A->B`表示B依赖于A,`{A,B}->C`表示C依赖于AB复合键

- 不符第2范式
    - {A,B}->D; B->C
    - solve: move B,C in new_table，B refered
- 不符第3范式
    - {A,B}->C; C->D
    - solve1: move C,D in new_table, C refered
    - solve2: {A,D}成为候选键，{A,D}->B; C->D
- 不符第3.5范式
    - {A,B}->D; C->B
    - solve: move C,B in new_table, C refered

### 非规范化

规范化会导致表数量不断增加，减慢查询时间。因此有时要特意非规范化

非规范化的特性：

- 会牺牲数据的完整性
- 难以理解
- 加快查询，降低更新速度
- 增加了插入不一致数据的风险
- 适用：应当只用于插入（如日志），而不能用来更新已有数据

## mySql

* 数据类型：INT，CHAR（max_char_number),一般用VARCHAR（动态大小），TEXT（0-65535字节），decimal（5， 2）共存5位数，2位小数
* 不区分大小写
* 使用`;`为一个命令结尾

mysql图形界面：navicat（解压后删除.navicat64，取消安装wine）
登陆: mysql -u root -p mysql

* 显示已有数据库： show databases;  // 以；结束命令输入
* 查看语句具体进行的操作，使用show： show create database base_name charset=utf8;
* 显示时间，版本： select now(); select version();  // 使用select选择函数来显示，而非show

1.数据库操作
* 注释： -- 注释内容
* 创建数据库： create database base_name charset=utf8; // charset默认为latin
* 删除数据库： drop database base_name  // 若数据库名带-，则需输入\`base-name\`。
* 使用数据库： use base_name
* 显示当前使用中的数据库名称： select database();  // 需先用use使用数据库。

2.
* 显示当前数据库的所有数据表： show tables;
* 创建数据表: create table [if not exist ]table_name(字段 类型 约束[, 字段 类型 约束]) [select语句];  // int unsigned
* 删除数据表： drop table table_name
* 查看表格本身（而非表中数据）的结构： desc table_name;  // desc是describe的缩写？

exp： 创建表格，插入数据实例

    drop table authors;
    create table authors
    (
        au_id char(3) not null,
        au_fname varchar(15) not null,
        au_lname varchar(15) not null,
        phone varchar(12),
        address varchar(20),
        city varchar(15),
        state char(2),
        zip char(5),
        constraint pk_authors primary key (au_id)
        );
    insert into authors value('A01','Franz','Kafka','','','Österreich-Ungarn','','');

3.修改表格结构（alter）
* 增加字段： alter table table_name add 字段名 类型及约束；
* 修改字段： alter table table_name modifiy 字段名 类型及约束；
* 修改已有字段为新字段： alter table table_name change 原字段 新字段名 类型及约束[ ,change 原字段 新字段名 类型及约束]；
* 删除字段： alter table table_name drop 字段名 类型及约束；  // 会将数据一并删除
* **链接到外键**： alter table table_1 add foreign key (需要被外键约束的字段） references table_2 (table_2中的字段）；
* **删除外键**： alter table table_1 drop foreign key 外键名称（需要先show create table table_1 找出外键约束名）；


4.数据修改（curd：create,update,retrive,delete)
* 显示整个表格的数据： select \* from table_name [where 字段=值];  //条件也可以是字段>值
* 插入数据： insert into table_name [(要插入数据的字段1， 字段2， 字段3)] values(具体数值）[,(具体数值)];
* 修改某一字段的数据： update students set 字段=值[,字段=值] where id=5;
* 删除数据： delete from table_name where 字段=值;  // 没有where就会删除所有数据
* **将查询结果插入表格**： insert into table_name [(要插入数据的字段)] select语句；
* **关联修改某一字段的数据**： update table_name as 别名 inner join table_2 on 条件 set 字段=值；

对于一个用户一般只标记已经删除而非真正删除。
alter table table_name add user_deleted bit default 0;
update table_name set user_deleted=1 where user_id=13; // 1表示账户已无效。

5.数据查询(select)
* select [distinct] 别名.字段[,别名.字段] from table_name as 别名；  // distinct去重

where 条件1 and 条件2;
where not (条件1 and 条件2);

1. 条件查询： 
* where 字段=值  -- 表示精确查询
* where 字段 like 值%  -- 表示模糊查询，%替换1或多个，_替换1个。
* where 字段 rlike 值%  -- 表示正则查询

2. 范围查询
* where 字段 not in (值1， 值2， 值3）；
* where [not] (字段 [not] between int1 and 值2);  // not可前可后，括号内为1个条件整体
* where 字段 is null；

6.对查询到的数据排序，在最后加上order
* order by 字段 asc/desc [,字段 asc/desc];  //先判断前边的条件（ascend，descend）

7.聚合函数(求和、求数量、求平均值等）、分组
* select count(*) from table_name where 条件；  // count计算数据条数
* select round(sum(字段)/count(*), 2) from table_name where 条件；
此时显示结果为1个值

* select **gender**, sum(age)/group_concat(name, " ", age)[,avg(age)] from table_name where 条件 group by **gender** having avg（age) > 20;  -- group字段为gender，所以前边的字段也要为gender

1. 先用where确定所选内容，
2. 使用group按字段中不同的值来分组。
3. 使用having仅显示符合筛选条件的组(筛选计算后的值）。
4. 对不同的组都1.求出值，或2.使用group_concat()显示组中的每条数据的字段内容。

7.分页
* 最后加上 limit 每页显示数量；
* 或者 limit 开始项， 每页显示数量； --开始项从0开始，放在order后边。

8.链接查询（多个表，会显示2个表的内容）
* select ... from table_1 [left] inner join table_2 on 条件;  // left表示显示table_1中的所有内容，table_2不符合条件的部分显示为null
* select table_1.字段/*，table2.字段 from table_1 left inner join table_2 on 条件/table_1.字段=table_2.字段 having 字段=null;

9.自关联（省市县）
使用链接查询，将1个表命名为2个别名作为2个表使用

10.子查询(效率较低）
将查询结果作为另一个查询的条件
* select * from students where height=(select max(height) from students);

### exp: 查询实例

    select [all|distinct] city as "c",
            code as "cd",
            au_name as "an",
            state
        from table_country
        order by 4 [asc | desc],
                 2 [asc | desc],
                 an [asc | desc];

默认为all，distinct表示去除重复项
TODO：测试是否每一列都可用distinct

as起别名后可供order使用

order by 的数字代替select中的列名。也可以输入全名。
NOTE：可用select的列(此处为c,cd,an,state)之外的列进行排序，但不建议使用
NOTE：null的排序取决于dbms，mysql与oracle的null排序不同

    select title,price,sales,
            price * sales As "total"
        from table_country
        ORDER BY CASE WHEN cd='213'
            THEN an ELSE city END;

NOTE:price*sales会相乘并将结果保存为虚拟的新列total（派生列
NOTE:可将sql关键字都大写以区分关键字。

### 条件筛选

形式： `WHERE col op value;`

    select title,price,sales,pub_date,product_date
            price * sales As "total"
        FROM table_country
        WHERE ((price * sales > 1000)
            AND (pub_date >= DATE '2003-02-07'))
            OR (title = "live")
            OR NOT (title = "fail")
            OR title LIKE '_ke%'
            OR product_date BETWEEN DATE '2001-03-08'
                            AND DATE '2002-03-08';

NOTE：用<>表示不等，而不是！=, 用=表示相等，而不是==


NOTE: 最好将语句放在()中

条件 | 等价于 |
--- | --- |
not (not p) | p
not (p and q) | (not p) or (not q)
not (p or q) | (not p) and (not q)

特殊操作符(<,>,>=之外)：like,between,in,is null

- LIKE进行相似匹配，其value为一个正则字符串,`_`匹配单个字符，`%`匹配任意数量的字符
	- where col like '%str%'
NOTE: 必须是date对象才能进行比较，因为2个字符串不能>,<比较
- between等同于where col>= val1 and col<=val2
- col in (val1,val2,val2)
- where col is null
NOTE: null值不进行任何匹配，>,<,=,<>等都不匹配null值,只有is null能确定是否为null

### 计算操作

    select f_name || ' ' || l_name
            AS full_name,
            SUBSTRING(pub_id from 2 for 4)
            AS "from 2 and select 4 chars",
            trim(leading 'H' from publisher)
        FROM authors
        WHERE EXTRACT(MONTH FROM pubdate)
            between 6 and 9
            and pubdate between
                (current_timestamp - interval 90 day)
                and (current_timestamp + interval 90 day)
        order by position('st' in f_name) asc

- `||`连接字符串获得作者全名
- substring()函数选取部分
- upper(),lower()修改大小写
- trim([[leading|trailing|both] ['trim_chars'] from] string/column),
删除前/后的trim_chars,默认为空格
- charactr_length()返回字符个数
- position(string in column)返回字符串第一次出现的位置
- extract(field from datetime_column_or_interval)提取时间
- current_date,current_time,current_timestamp获取当前时间,current_time(6)为秒添加6位精度
- CURRENT_USER为当前用户
- cast(column as data_type)类型转换
case同C++中的case

	select
		condi,
		price
		case condi
			when "good" then price*1.5
			when "bad" then price*0.8
			else price
		END
			as 'new_price'

- coalesce(state,user 'N/A') as "not_null_col",检测每项是否为空值，都不能匹配则填充最后一个值
- nullif(exp1,exp2) as "eq is null",exp1,2相等则返回空值，否则返回exp1的值

### 汇总和分组

聚合函数，min,max,sum,avg,count都忽略空值，除了count(*),count返回行数

特性：
- 聚合表达式不可出现在where语句中
- select作用域中，仅分组列可混合使用费聚合表达式和聚合表达式
- 聚合函数不可嵌套（因为聚合函数处理一系列值，返回一个值，再嵌套没有意义）

NOTE：where语句生效之后再进行聚合计算

先distinct column,再进行聚合计算，否则没有意义
select
	count(distinct price)

#### 分组

group by:相同值的被分为一组,count(sales)会为每一组进行计算
想显示多列则都要进行分组，若只group au_id，则pub_id列就不知道该填什么

    select au_id,pub_id count(sales) as "numbooks"
        from title_authors
        group by au_id,pub_id

    select 
        case
            when sales is null
                then 'unknown'
            when sales <= 1000
                then 'no more than 1000'
            when sales <= 10000
                then '1000-10000'
            else 'over 10000'
        END
            as 'sales category'
        count(*) as 'num titles'
    from titles
    group by
        'sales category'
    order by min(sales) asc; 

hacing: group后会有多个group,having通常对每个group进行操作，以筛选所需的group，因此一般用聚合函数

	select
		type,count(price) as "pri",
		avg(price*sales) as 'avg recenue'
	from titles
	group by type
	having avg(price * sales) > 10000
		and avg(price) > 200;

### 联结

作用:从多个表中检索行并以一张表展现

1. 限定列名 table.column,无歧义且提高性能

`from table_name alias`可设置table别名为alias 

	select au_id,a.city
		from authors a
		inner join publishers p
			on a.city = p.city;

联结类型 | description |
--- | --- |
cross join | 显示表1的每行和表2的所有行组合得到的所有行
inner join | 用比较操作符比较2个表共同列的值，显示与操作符匹配的行
natural join | 是inner join的一种，使用=比较操作符（不可修改）,只保留1列相同的列（主键列）
left outer join | 返回左表所有select列的行,右表符合on条件的显示值，否则显示null
right outer join | 与left outer join相反
full outer join | 是左右联结的并集
self-join | 自联结


exp:Before
NOTE:select * 时默认比较主键

class table
ID | NAME |
--- | --- |
1 | abhi
2 | adam
3 | anu

class_info table
ID | Address |
--- | --- |
1 | DELHI
2 | MUMBAI
3 | CHENNAI

	SELECT * FROM class CROSS JOIN class_info;

ID | NAME | ID | Address |
--- | --- | --- | --- |
1 | abhi | 1 | DELHI
2 | adam | 1 | DELHI
4 | alex | 1 | DELHI
1 | abhi | 2 | MUMBAI
2 | adam | 2 | MUMBAI
4 | alex | 2 | MUMBAI
1 | abhi | 3 | CHENNAI
2 | adam | 3 | CHENNAI
4 | alex | 3 | CHENNAI

exp:Before

修改 class table为
ID | NAME |
--- | --- |
1 | abhi
2 | adam
3 | alex
4 | anu

	SELECT * from class INNER JOIN class_info
		where class.id = class_info.id;

ID | NAME | ID | Address |
--- | --- | --- | --- |
1 | abhi | 1 | DELHI
2 | adam | 2 | MUMBAI
3 | alex | 3 | CHENNAI

	SELECT * from class NATURAL JOIN class_info;

ID | NAME | Address |
--- | --- | --- |
1 | abhi | DELHI
2 | adam | MUMBAI
3 | alex | CHENNAI

exp:Outer join Before

修改 class table为
ID | NAME |
--- | --- |
1 | abhi
2 | adam
3 | alex
4 | anu
5 | ashish

修改 class_info table为
ID | Address |
--- | --- |
1 | DELHI
2 | MUMBAI
3 | CHENNAI
7 | NOIDA
8 | PANIPAT

	SELECT * FROM class 
		LEFT OUTER JOIN class_info 
			ON (class.id = class_info.id);


ID | NAME | ID | Address |
--- | --- | --- | --- |
1 | abhi | 1 | DELHI
2 | adam | 2 | MUMBAI
3 | alex | 3 | CHENNAI
4 | anu | null | null
5 | ashish | null | null

	SELECT * FROM class FULL OUTER JOIN class_info ON (class.id = class_info.id);

ID | NAME | ID | Address
--- | --- | --- | --- |
1 | abhi | 1 | DELHI
2 | adam | 2 | MUMBAI
3 | alex | 3 | CHENNAI
4 | anu | null | null
5 | ashish | null | null
null | null | 7 | NOIDA
null | null | 8 | PANIPAT



11.数据库（数据表）设计
1. 第一范式： 不能再拆分
2. 第二范式： 表必须有1个主键。没有包含在主键中的列必须完全依赖于主键，而不能只依赖于主键的一部分。
3. 另外非主键列必须直接依赖于主键，不能存在传递依赖。即不能存在：非主键列A依赖于非主键列B，B依赖于主键的状况。

E-R模型
E表示entry/实体，像定义类一样，
R表示relationship/关系，描述两个实体间的对应规则，关系有1对1，多对多，1对多。关系也是一种数据，需要存储

***
* as: 起别名
* where： 筛选每条数据符合的条件
* having： 筛选计算后的结果作为条件
* on： 筛选表与表间的符合条件的项。（也可以是1个表的2个别名）
***

### 3.mysql与python

```python
from mysql import *
conn = connect(host='localhost', port=3305, user='root', password='mysql', database='jindong', charset='utf8')
curs1 = conn.cursor()
curs1.execute('''sql code''')  # 执行后得到1张元组表，由多个元组构成
curs1.fetch()  # 获取1个元组
curs1.fetchmany(3)  # 获取3个元组
curs1.fetchall()
conn.commit()  # 提交之前做的所有修改，真正写入数据库
conn.rollback()  # 取消这条语句到上一个conn.commit()间的所有修改语句，但有auto_increment的字段不commit也会增加
cur1.close()  # 这两条写到__delete__方法中，自动调用
conn.close()
```
### 防止SQL注入，巫云
> 可构造一个列表或元组存储外界输入信息

```mysql
qe = input("输入商品名")
sql = """select * from goods where name='%s'"""
curs1.excecute(sql, [qe])  // 构造参数列表
sql_注入 = ' or 1=1 or '1
若不安全就会 执行 
select * from goods where name='' or 1=1 or '1'
此时1=1成立
```

### 4.高级
1.视图：curs1.execute('''sql code''')后返回的结果的虚拟的表,会根据表数据变化相应的变化。不可再视图中修改原表数据。
创建视图: create view v_tablename as select语句

2.事务：操作序列。序列中的语句全部执行或全不执行。银行的资金转移
原子性、一致性、隔离性、持久性《高性能sql》
```sql
start transaction; --或者 begin；
--多条sql语句
commit；
```

3.索引:提高查询效率（但影响update和insert的速度）
是一种特殊的文件（innoDB数据表上的索引是表空间的一个组成部分），它们包含对数据表里所有记录的引用指针。
开启运行时间的监测：set profiling=1;
查看执行时间：show profiles;
创建索引：create index index_name on table_name(字段（[字符串类型的数据长度]））;

原理：不断缩小想要获得的数据的范围，同时把随机事件变成顺序事件。

4.账户管理(user也是一个数据库)：
查看用户： desc user;
* select host, user, authentication_string from user;
创建账户并授予权限：
* grant select,insert on database_name.* to 'new_user_name'@'localhost/%/具体ip' identified by 'password';  // select,insert只授予查询和插入数据的权限，可换成all privileges，%表示可从任何ip登陆

* 查看用户权限： grant user_name

* 修改权限: grant select on database to 'user_name'@'ipaddress' with grant option;
* 刷新权限：flush privileges;
* 修改用户密码： update user set authentication_string=password('new_password') where user='user_name';
* 删除账户1：drop user 'user_name'@'ipaddress';
* 删除账户2：delete from user where user='user_name';

* 先将/etc/mysql/mysql.conf.d/mysqld.cnf的bind-addr = 127.0.0.1用#注释
* 远程登陆（应当ssh登陆电脑，而非直接远程登陆数据库）： mysql -h172.16.7.137 -unew_user_name -p

5.mysql主从（自动备份）
* 手动备份： mysqldump -uroot -p database_name > a_back_file.sql;
* 恢复数据： mysql -uroot -p new_database_name < a_back_file.sql;
导出的sql文件内容格式（包含表信息）：
1. drop table if exist
2. create table
3. insert into table

* 在主服务器上备份：mysqldump -uroot -ppass_word --all-databases --lock-all-tables > ~/path/a_back_file.sql;  --此时输出还包含了数据库名
* 在从服务器上恢复数据： mysql -uroot -ppass_word < a_back_file.sql;  --无需数据库名
* 配置主服务器：sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf 将server-id和log_bin去除注释
* 配置从服务器：sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf 将server-id改为不同值
* 重启mysql服务： sudo service mysql restart
* 主服务器创建新用户： grant replication slave on *.* to 'slave_name'@'%' identified by 'password';
* 查看主服务器信息： show master status;
* ubantu从服务器先登陆自己的root,然后连接到主服务器： change master to master_host='host_ip',master_user='username',master_password='password',master_log_file='mysql-bin.00006',master_log_pos=590;
* 查看从服务器查看信息： show slave status \G; --slave I/O running,slave sql running 表示连接成功

配置windows从服务器：
1. C/ProgramData/MySQL/MySQL Server 5.7/my.ini修改server-id
2. services.msc打开MySQL57服务
3. 其他相同
