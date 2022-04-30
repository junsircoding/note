# Redis

## 1.数据操作

### 1.1-string类型

- ### 保存

- 设置键值

``````bash
set key value
``````

- 例1：设置键为name值为itcast的数据

``````bash
set name itcast
``````

- 设置键值及过期时间，以秒为单位

``````bash
setex key seconds value
``````

- 例2：设置键为aa值为aa过期时间为3秒的数据

``````bash
setex aa 3 aa
``````

- 设置多个键值

``````bash
mset key1 value1 key2 value2 ...
``````

- 例3：设置键为'a1'值为'python'、键为'a2'值为'java'、键为'a3'值为'c'

``````bash
mset a1 python a2 java a3 c
``````

- 追加值

``````bash
append key value
``````

- 例4：向键为a1中追加值' haha'

``````bash
append 'a1' 'haha'
``````

- ### 获取

- 获取：根据键获取值，如果不存在此键则返回nil

``````bash
get key
``````

- 例5：获取键'name'的值

``````bash
get 'name'
``````

- 根据多个键获取多个值

``````bash
mget key1 key2 ...
``````

- 例6：获取键a1、a2、a3'的值

``````bash
mget a1 a2 a3
``````

### 1.2-键命令

- 查找键，参数⽀持正则表达式

``````bash
keys pattern
``````

- 例1：查看所有键

``````bash
keys *
``````

- 例2：查看名称中包含a的键

``````bash
keys 'a*'
``````

- 判断键是否存在，如果存在返回1，不存在返回0

``````bash
exists key1
``````

- 例3：判断键a1是否存在

``````bash
exists a1
``````

- 查看键对应的value的类型

``````bash
type key
``````

- 例4：查看键a1的值类型，为redis⽀持的五种类型中的⼀种

``````bash
type a1
``````

- 删除键及对应的值

``````bash
del key1 key2 ...
``````

- 例5：删除键a2、a3

``````bash
del a2 a3
``````

- 设置过期时间，以秒为单位
- 如果没有指定过期时间则⼀直存在，直到使⽤DEL移除

``````bash
expire key seconds
``````

- 例6：设置键'a1'的过期时间为3秒

``````bash
expire 'a1' 3
``````

- 查看有效时间，以秒为单位

``````bash
ttl key
``````

- 例7：查看键'bb'的有效时间

``````bash
ttl bb
``````

### 1.3-hash类型

- hash⽤于存储对象，对象的结构为属性、值
- 值的类型为string

- ### 增加、修改

- 设置单个属性

``````bash
hset key field value
``````

- 例1：设置键 user的属性name为test

``````bash
hset user name test
``````

- 设置多个属性


``````bash
hmset key field1 value1 field2 value2 ...
``````

- 例2：设置键u2的属性name为itcast、属性age为11


``````bash
hmset u2 name itcast age 11
``````

- ### 获取

- 获取指定键所有的属性


``````bash
hkeys key
``````

- 例3：获取键u2的所有属性


``````bash
hkeys u2
``````

- 获取⼀个属性的值


``````bash
hget key field
``````

- 例4：获取键u2属性'name'的值


``````bash

``````

- 获取多个属性的值


``````bash

``````

- 例5：获取键u2属性'name'、'age的值


``````bash
hmget u2 name age
``````

- 获取所有属性的值


``````bash
hvals key
``````

- 例6：获取键'u2'所有属性的值

``````bash
hvals u2
``````

- ### 删除

- 删除整个hash键及值，使⽤del命令
- 删除属性，属性对应的值会被⼀起删除

``````bash
hdel key field1 field2 ...
``````

- 例7：删除键'u2'的属性'age'

``````bash
hdel u2 age
``````

### 1.4-list类型

- 列表的元素类型为string
- 按照插⼊顺序排序

- ### 增加

- 在左侧插⼊数据


``````bash
lpush key value1 value2 ...
``````

- 例1：从键为'a1'的列表左侧加⼊数据a 、 b 、c


``````bash
lpush a1 a b c
``````

- 在右侧插⼊数据


``````bash
rpush key value1 value2 ...
``````

- 例2：从键为'a1'的列表右侧加⼊数据0 1


``````bash
rpush a1 0 1
``````

- 在指定元素的前或后插⼊新元素


``````bash
linsert key before或after 现有元素 新元素
``````

- 例3：在键为'a1'的列表中元素'b'前加⼊'3'


``````bash
linsert a1 before b 3
``````

- ### 获取

- 返回列表⾥指定范围内的元素

  - start、stop为元素的下标索引
  - 索引从左侧开始，第⼀个元素为0
  - 索引可以是负数，表示从尾部开始计数，如-1表示最后⼀个元素


``````bash

``````

- 例4：获取键为'a1'的列表所有元素


``````bash

``````

- ### 设置指定索引位置的元素值

- 索引从左侧开始，第⼀个元素为0

- 索引可以是负数，表示尾部开始计数，如-1表示最后⼀个元素


``````bash
lset key index value
``````

- 例5：修改键为'a1'的列表中下标为1的元素值为'z'


``````bash
lset a 1 z
``````

- ### 删除

- 删除指定元素

  - 将列表中前count次出现的值为value的元素移除
  - count > 0: 从头往尾移除
  - count < 0: 从尾往头移除
  - count = 0: 移除所有


``````bash
lrem key count value
``````

- 例6.1：向列表'a2'中加⼊元素'a'、'b'、'a'、'b'、'a'、'b'


```bash
lpush a2 a b a b a b
```

- 例6.2：从'a2'列表右侧开始删除2个'b'


```bash
lrem a2 -2 b
```

- 例6.3：查看列表'py12'的所有元素


```bash
lrange a2 0 -1
```

### 1.5-set类型

- ⽆序集合
- 元素为string类型
- 元素具有唯⼀性，不重复
- 说明：对于集合没有修改操作

- ### 增加

- 添加元素

```bash
sadd key member1 member2 ...
```

- 例1：向键'a3'的集合中添加元素'zhangsan'、'lisi'、'wangwu'

```bash
sadd a3 zhangsan sili wangwu
```

- ### 获取

- 返回所有的元素

```bash
smembers key
```

- 例2：获取键'a3'的集合中所有元素

```bash

```

- ### 删除

- 删除指定元素

```bash
srem key
```

- 例3：删除键'a3'的集合中元素'wangwu'

```bash
srem a3 wangwu
```

### 1.6-zset类型

- sorted set，有序集合
- 元素为string类型
- 元素具有唯⼀性，不重复
- 每个元素都会关联⼀个double类型的score，表示权重，通过权重将元素从⼩到⼤排序
- 说明：没有修改操作

- ### 增加

- 添加

```bash
zadd key score1 member1 score2 member2 ...
```

- 例1：向键'a4'的集合中添加元素'lisi'、'wangwu'、'zhaoliu'、'zhangsan'，权重分别为4、5、6、3

```bash

```

- ### 获取

- 返回指定范围内的元素
- start、stop为元素的下标索引
- 索引从左侧开始，第⼀个元素为0
- 索引可以是负数，表示从尾部开始计数，如-1表示最后⼀个元素

```bash
zrange key start stop
```

- 例2：获取键'a4'的集合中所有元素

```bash
zrange a4 0 -1
```

- 返回score值在min和max之间的成员


```bash
zrangebyscore key min max
```

- 例3：获取键'a4'的集合中权限值在5和6之间的成员


```bash

```

- 返回成员member的score值


```bash
zscore key member
```

- 例4：获取键'a4'的集合中元素'zhangsan'的权重


```bash

```

- ### 删除

- 删除指定元素


```bash

```

- 例5：删除集合'a4'中元素'zhangsan'


```bash

```

- 删除权重在指定范围的元素


```bash
zremrangebyscore key min max
```

- 例6：删除集合'a4'中权限在5、6之间的元素


```bash
zremrangebyscore a4 5 6
```

## 2.与Python交互

- ### 调⽤模块

- 引⼊模块

```python
from redis import *
```

- 这个模块中提供了StrictRedis对象(Strict)，⽤于连接redis服务器，并按照不同类型提供了不同⽅法，进⾏交互操作

### StrictRedis对象⽅法

- 通过init创建对象，指定参数host、port与指定的服务器和端⼝连接，host默认为localhost，port默认为6379，db默认为0
- Redis默认有16个数据库,可按需求分类存储不同数据,指定不同的数据库**db=0-15**

```python
sr = StrictRedis(host='localhost', port=6379, db=0)

简写
sr=StrictRedis()
```

- 根据不同的类型，拥有不同的实例⽅法可以调⽤，与前⾯学的redis命令对应，⽅法需要的参数与命令的参数⼀致

### string-增加

- ⽅法set，添加键、值，如果添加成功则返回True，如果添加失败则返回False
- 编写代码如下

```python
from redis import *
if __name__=="__main__":
    try:
        #创建StrictRedis对象，与redis服务器建⽴连接
        sr=StrictRedis()
        #添加键name，值为test
        result=sr.set('name','test')
        #输出响应结果，如果添加成功则返回True，否则返回False
        print(result)
    except Exception as e:
        print(e)
```

### string-获取

- ⽅法get，添加键对应的值，如果键存在则返回对应的值，如果键不存在则返回None
- 编写代码如下

```python
from redis import *
if __name__=="__main__":
    try:
        #创建StrictRedis对象，与redis服务器建⽴连接
        sr=StrictRedis()
        #获取键name的值
        result = sr.get('name')
        #输出键的值，如果键不存在则返回None
        print(result)
    except Exception as e:
        print(e)
```

### string-修改

- ⽅法set，如果键已经存在则进⾏修改，如果键不存在则进⾏添加
- 编写代码如下

```python
from redis import *
if __name__=="__main__":
    try:
        #创建StrictRedis对象，与redis服务器建⽴连接
        sr=StrictRedis()
        #设置键name的值，如果键已经存在则进⾏修改，如果键不存在则进⾏添加
        result = sr.set('name','itcast')
        #输出响应结果，如果操作成功则返回True，否则返回False
        print(result)
    except Exception as e:
        print(e)
```

### string-删除

- ⽅法delete，删除键及对应的值，如果删除成功则返回受影响的键数，否则则返 回0
- 编写代码如下

```python
from redis import *
if __name__=="__main__":
    try:
        #创建StrictRedis对象，与redis服务器建⽴连接
        sr=StrictRedis()
        #设置键name的值，如果键已经存在则进⾏修改，如果键不存在则进⾏添加
        result = sr.delete('name')
        #输出响应结果，如果删除成功则返回受影响的键数，否则则返回0
        print(result)
    except Exception as e:
        print(e)
```

### 获取键

- ⽅法keys，根据正则表达式获取键
- 编写代码如下

```python
from redis import *
if __name__=="__main__":
    try:
        #创建StrictRedis对象，与redis服务器建⽴连接
        sr=StrictRedis()
        #获取所有的键
        result=sr.keys()
        #输出响应结果，所有的键构成⼀个列表，如果没有键则返回空列表
        print(result)
    except Exception as e:
        print(e)
```

