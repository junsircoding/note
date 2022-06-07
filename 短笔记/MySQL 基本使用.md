MySQL 基本使用

MySQL 5.1 参考手册

查看 MySQL 服务状态

```shell
sudo service mysql status
```

停止 MySQL 服务

```shell
sudo service mysql stop
```

开启 MySQL 服务

```shell
sudo service mysql start
```

重启 MySQL 服务

```shell
sudo service mysql restart
```

MySQL 配置文件

```shell
/etc/mysql/mysql.conf.d/mysqld.cnf
```

MySQL 使用帮助

```shell
mysql --help
```

MySQL 登录

```shell
mysql -u[用户名] -p[密码]
```

显示当前时间

```sql
select now();
```

退出数据库

```shell
quit
exit
ctrl d
```

查看所有数据库

```shell
show databases;
```

创建数据库

```sql
create database 数据库名 charset=utf8;
```

使用数据库

```sql
use database()
```

查看当前使用的数据库

```sql
select database()
```

删库

``sql
drop database [数据库名];
```

查看当前数据库中所有表

```sql
show tables;
```

建表

```sql
create table 表名 (
    id int unsigned primary key auto_increment not null,
    name varchar(20) not null,
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男', '女', '保密')
);
```

修改表-添加字段

```sql
alter table 表名 add 添加的字段 类型 约束;
alter table mytable add birthday datetime not null;
```

修改表-修改字段类型

```sql
alter table 表名 modify 修改的字段 类型 约束;
```

修改表-修改表名

```sql
alter table 表名 change 旧名 新名 类型 约束;
```

修改表-删除字段

```sql
alter table 表名 drop 字段名;
```

查看创表语句

```sql
show create table 表名;
```

查看创库语句

```sql
show create database 库名;
```

删除表

```sql
drop table [表名];
```

查数据

```sql
select * from [表名];
```

插入数据
全列插入不写表头
可同时插入多条数据    
逻辑删除

```sql
alter table [表名] add isdelete bit default 0;
update table [表名] set 字段名=1 where id =id值
```
 
给字段取别名

```sql
select id as [学号], name form [表名];
```

给表取别名

```sql
select s.x, s.x from [表名] as s;
```

去重

```sql
select distint name, gender from students;
```

模糊查询

```shell
% 匹配任意个字符
_ 匹配一个字符
```

```sql
select * from [表名] where name like '黄%';
select * from [表名] where name like '黄_';
```

指定范围查询

```sql
select * from students where id between 3 and 8;
```

排序查询

```sql
select * from students order by desc;
select * from students order by asc;
```

分页

```sql
select * from students where gender =1 limit 0,3;
select * from students where gender =1 limit 从哪开始，共几条;
```

查询学生表，获取第n页数据的m条数据

```sql
select * from students where gender =1 limit (n-1)*m，m;
```

函数

```sql
count()
max()
min()
sum()
avg()
```

mysqldump 导出【指定数据库】的【每个表】的【前n条数据】

```shell
mysqldump  -P [端口] -h [IP] -u[用户名] -p[密码] [库名] --where="true limit 100" > bak.sql
mysqldump  -P [端口] -h [IP] -u[用户名] -p[密码] [库名] --where "1=1 limit 100" --lock-all-tables > bak.sql
```

导出【指定数据库】的【所有表结构】

```shell
mysqldump -P [端口] -h [IP]  -u[用户名] -p[密码] -d [库名] > bak.sql;
```

导出【指定数据库】的【指定表】的【表结构】
```shell
mysqldump -P [端口] -h [IP] -u[用户名] -p[密码] -d [库名] [表名] > bak.sql;
```

导出【指定数据库】的【所有表结构及表数据】（不加-d）
```shell
mysqldump -P [端口] -h [IP] -u[用户名] -p[密码]  [库名] > bak.sql;
```

导出【指定数据库】的【所有表结构及表数据】（不加-d）
```shell
mysqldump -P [端口] -h [IP] -u[用户名] -p[密码] [库名] [表名] > bak.sql;
```

查询 mysql 数据表中的最后一条记录
```sql
select * from [表名] order by [字段名] DESC limit 1;
```
