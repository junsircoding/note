SQLAlchemy Core 笔记

数据库管理涉及到对**表**的增删改查和对**表数据**的增删改查。

### 对表的增删改查

```python
from sqlalchemy import create_engine, MetaData, Table, inspectfrom sqlalchemy.ext.declarative import declarative_base
# 获取引擎
engine = create_engine('postgresql+psycopg2://【用户名】:【密码】@【ip地址】:【端口】/【库名】', echo=False)
# 查表
engine.table_names()
# 获取表对象
tb = Table('【表名】', meta, autoload=True, autoload_with=engine)
# 表col列表
cols = [col.name for col in tb.columns]
# 联合唯一索引
insp = inspect(engine)
insp.get_unique_constraints('【表名】')
# 建表
meta = MetaData()
new_tb = Table('【表名】', meta, 【字段列表，形式同model】)
meta.create_all(engine)

# 删表
tb.drop(engine)
# 改表
alembic
# 运行sql
conn = engine.connect()
with conn.begin() as trans:
    conn.execute(r'''
           INSERT INTO user VALUES (：1 ：2 ：3 ：4 ：5)
           ''', ('aa', 'BUY', 'RHAT', 100, 35.14))
    trans.commit()
```

### 对表数据的增删改查

```python
#查数据
from sqlalchemy.sql import select, cast
conn = engine.connect()

tb = Table('【表名】', meta, autoload=True, autoload_with=engine)
# 全查
query = select([tb])


# 指定某几列全查
query = select([tb.c['【列名】'], tb.c['【列名】']])
# 筛查
query = query.where(tb.c['【列名】'] ==【关键字】)
# 模糊查
query = query.where(tb.c['【列名】'].like('%【关键字】%'))

# 查询结果一律按照字符串处理
query = query.where(cast(tb.c['【列名】'], String) == 【关键字】)
# 分页
query = query.limit(page_size).offset(page_index * page_size)

# 执行查询返回结果集
result = conn.ececute(query)
# 结果条数
result.rowcount
# 结果构造成字典
table_records = []

for raw in result:
    table_records.append(dict(zip(raw.keys(), raw.values())))
# 添加数据
conn.execute(tb.insert(), 【数据字典，键为列名】)
# 更新数据

stmt = tb.update().where(tb.c['【列名】']==【关键字】).values(【数据字典，键为列名】)
conn.execute(stmt, 【数据字典，键为列名】)
# 删除数据
conn.execute(tb.delete().where(tb.c['【列名】']==【关键字】))

orm 方式还可以这样改：
user = orm.query(User).filter(User.id=123).one()
update_dict = {"name":"tom", "age":"34"}
for k, v in update_dict:
    setattr(user, k, v)
```

### SqlAlchemy 内置字段

| 表的属性 | 含义 |
| --- | --- |
| tb.alias | 给这个表取一个别名 |
| tb.append_column |  给这个表加一列，`tb.append_column(Column('i_am_new_col', VARCHAR(255), nullable=False))`，如果重复不报错直接覆盖，只是在内存中，未提交 |
| tb.c |  同tb.columns，返回列的可迭代对象 |
| tb.columns |  返回列的可迭代对象 |
| tb.fullname |  返回表名 |
| tb.key |  返回表名 |
| tb.name |  返回表名 |
| tb.primary_key |  判断是否为主键 |

### SQLAlchemy create_engine 函数解析

这个函数会创建一个 _engine.Engine 实例。

标准的调用形式是将URL作为第一个位置参数发送，通常是一个表示数据库方言和连接参数的字符串。

```python
engine = create_engine("postgresql://scott:tiger@localhost/test")
```

其他的参数可以配置引擎、方言和连接池。

```python
engine = create_engine("mysql://scott:tiger@hostname/dbname",
encoding='latin1', echo=True)
```

URL 的格式

```python
dialect[+driver]://user:password@host/dbname[?key=value..]
```
dialect：数据库名称，如 mysql、oracle、postgresql
driver：DBAPI 的名称，如 psycopg2、pyodbc、cx_oracle
另外，URL 可以是一个实例：~sqlalchemy.engine.url.URL

其他参数对应可以配置更多的选项，下面具体描述。
case_sensitive：True/False
取列名时大小写敏感

connect_args：字典
一个选项字典，它将作为附加的关键字参数直接传递给DBAPI的 connect() 方法

convert_unicode：False/True
将所有 String 数据类型转为 unicode。此参数新版本要删掉。

creator
忽略传入的 URL，从底层连接池找连接对象。

echo：True/False
打印详细日志，包含执行的 sql

echo_pool：True/False
打印连接池的详细日志

empty_in_strategy：static/dynamic/dynamic_warn
在使用 in_ 表达式时，会遇到与空集合比较的情况。这个参数用来指定此时的策略。
默认是 static，与空集合比较会生成一个简单的错误表达式 1 != 1
dynamic，发出一个形式为"expr != expr"的假表达式，在NULL表达式的情况下，它的计算结果为NULL
dynamic_warn，功能与 dynamic 相同，但会告警

encoding
编码，默认 utf-8