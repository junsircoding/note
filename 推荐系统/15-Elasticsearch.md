# Elasticsearch

You know, for search!       

文档 <https://www.elastic.co/guide/cn/elasticsearch/guide/current/index.html>

2.x

5.x  

6.x

### 1 简介

**Elasticsearch是一个基于Lucene库的搜索引擎。**

它提供了一个分布式、支持多用户的全文搜索引擎，**具有HTTP Web接口和无模式JSON文档。**所有其他语言可以使用 **RESTful API 通过端口 *9200* 和 Elasticsearch 进行通信**  haystack

**Elasticsearch是用Java开发的**，并在Apache许可证下作为开源软件发布。官方客户端在Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby和许多其他语言中都是可用的。

根据DB-Engines的排名显示，**Elasticsearch是最受欢迎的企业搜索引擎**，其次是Apache Solr，也是基于Lucene。

Elasticsearch可以用于搜索各种文档。它提供可扩展的搜索，具有接近实时的搜索，并支持多租户。

**Elasticsearch是分布式的**，这意味着索引可以被分成分片，每个分片可以有0个或多个副本。每个节点托管一个或多个分片，并充当协调器将操作委托给正确的分片。再平衡和路由是自动完成的。相关数据通常存储在同一个索引中，该索引由一个或多个主分片和零个或多个复制分片组成。一旦创建了索引，就不能更改主分片的数量。

**Elasticsearch 是一个实时的分布式搜索分析引擎，它被用作全文检索、结构化搜索、分析以及这三个功能的组合**

- Wikipedia 使用 Elasticsearch 提供带有高亮片段的全文搜索，还有 *search-as-you-type* 和 *did-you-mean* 的建议。
- *卫报* 使用 Elasticsearch 将网络社交数据结合到访客日志中，实时的给它的编辑们提供公众对于新文章的反馈。
- Stack Overflow 将地理位置查询融入全文检索中去，并且使用 *more-like-this* 接口去查找相关的问题与答案。
- GitHub 使用 Elasticsearch 对1300亿行代码进行查询。

 Lucene 仅仅只是一个库，然而，Elasticsearch 不仅仅是 Lucene，并且也不仅仅只是一个全文搜索引擎。 它可以被下面这样准确的形容：

- 一个分布式的实时文档存储，*每个字段* 可以被索引与搜索
- 一个分布式实时分析搜索引擎
- 能胜任上百个服务节点的扩展，并支持 PB 级别的结构化或者非结构化数据

##### 属于面向文档的数据库

Elasticsearch 是 *面向文档* 的，意味着它存储整个对象或 *文档_。Elasticsearch 不仅存储文档，而且 _索引*每个文档的内容使之可以被检索。在 Elasticsearch 中，你 对文档进行索引、检索、排序和过滤--而不是对行列数据。

### 2 搜索的原理——倒排索引（反向索引）、分析、相关性排序

#### 倒排索引 

倒排索引（英语：**Inverted index**），也常被称为**反向索引**、置入档案或反向档案，是一种索引方法，被用来存储在全文搜索下某个单词在一个文档或者一组文档中的存储位置的映射。**它是文档检索系统中最常用的数据结构。**

假设我们有两个文档，每个文档的 `content` 域包含如下内容：

1. The quick brown fox jumped over the , lazy+ dog 
2. Quick brown foxes leap over lazy dogs in summer

正向索引： 存储每个文档的单词的列表

```
Doc	  Quick  The brown dog	dogs  fox foxes in jumped lazy leap over quick summer the
--------------------------------------------------------------------------------------
Doc_1 |  	 |  X  |	X	|	 X |		|	X	 |		|		 |	X	 |	X	 |		|	X	 | X  |		  |  X
Doc_2	|	 X |		 |	X	|		 |	X	|		 |	X	|	X  |		 |	X	 |	X	|	X	 |    |		X	|
```

反向索引：

```
Term      Doc_1  Doc_2
-------------------------
Quick   |       |  X
The     |   X   |
brown   |   X   |  X
dog     |   X   |
dogs    |       |  X
fox     |   X   |
foxes   |       |  X
in      |       |  X
jumped  |   X   |
lazy    |   X   |  X
leap    |       |  X
over    |   X   |  X
quick   |   X   |
summer  |       |  X
the     |   X   |
------------------------
```

如果我们想搜索 `quick brown` ，我们只需要查找包含每个词条的文档：

```
Term      Doc_1  Doc_2
-------------------------
brown   |   X   |  X
quick   |   X   |
------------------------
Total   |   2   |  1
```

两个文档都匹配，但是第一个文档比第二个匹配度更高。如果我们使用仅计算匹配词条数量的简单 *相似性算法* ，那么，我们可以说，对于我们查询的相关性来讲，第一个文档比第二个文档更佳。

#### 分析

上面不太合理的地方：

- `Quick` 和 `quick` 以独立的词条(token)出现，然而用户可能认为它们是相同的词。
- `fox` 和 `foxes` 非常相似, 就像 `dog` 和 `dogs` ；他们有相同的词根。
- `jumped` 和 `leap`, 尽管没有相同的词根，但他们的意思很相近。他们是同义词。

进行**标准化**：

- `Quick` 可以小写化为 `quick` 。
- `foxes` 可以 *词干提取* --变为词根的格式-- 为 `fox` 。类似的， `dogs` 可以为提取为 `dog` 。
- `jumped` 和 `leap` 是同义词，可以索引为相同的单词 `jump` 。

标准化的反向索引：

```
Term      Doc_1  Doc_2
-------------------------
brown   |   X   |  X
dog     |   X   |  X
fox     |   X   |  X
in      |       |  X
jump    |   X   |  X
lazy    |   X   |  X
over    |   X   |  X
quick   |   X   |  X
summer  |       |  X
the     |   X   |  X
------------------------
```

**对于查询的字符串必须与词条（token）进行相同的标准化处理，才能保证搜索的正确性。**

分词和标准化的过程称为 *分析* （analysis） ：

- 首先，将一块文本分成适合于倒排索引的独立的 *词条* ， -> **分词**
- 之后，将这些词条统一化为标准格式以提高它们的“可搜索性”  -> **标准化**

分析工作是由**分析器** 完成的：   analyzer

- 字符过滤器

  首先，字符串按顺序通过每个 *字符过滤器* 。他们的任务是在分词前整理字符串。一个字符过滤器可以用来去掉HTML，或者将 `&` 转化成 `and`。

- 分词器

  我 是 中国  人  中国人  国人

  其次，字符串被 *分词器* 分为单个的词条。一个简单的分词器遇到空格和标点的时候，可能会将文本拆分成词条。

- Token 过滤器 （词条过滤器）

  最后，词条按顺序通过每个 *token 过滤器* 。这个过程可能会改变词条（例如，小写化 `Quick` ），删除词条（例如， 像 `a`， `and`， `the` 等无用词），或者增加词条（例如，像 `jump` 和 `leap` 这种同义词）。

#### 相关性排序

默认情况下，搜索结果是按照 ***相关性*** 进行倒序排序的——最相关的文档排在最前。

相关性可以用相关性评分表示，评分越高，相关性越高。

评分的计算方式取决于查询类型 不同的查询语句用于不同的目的： `fuzzy` 查询（模糊查询）会计算与关键词的拼写相似程度，`terms` 查询（词组查询）会计算 找到的内容与关键词组成部分匹配的百分比，但是通常我们说的 相关性 是我们用来计算全文本字段的值相对于全文本检索词相似程度的算法。

Elasticsearch 的相似度算法 被定义为检索词频率/反向文档频率， *TF/IDF* ，包括以下内容：

- 检索词频率

  检索词在该字段出现的频率？出现频率越高，相关性也越高。 字段中出现过 5 次要比只出现过 1 次的相关性高。

- 反向文档频率

  每个检索词在索引中出现的频率？频率越高，相关性越低。检索词出现在多数文档中会比出现在少数文档中的权重更低。

- 字段长度准则

  字段的长度是多少？长度越长，相关性越低。 检索词出现在一个短的 title 要比同样的词出现在一个长的 content 字段权重更大。 中国人        人   中国

### 3 概念

存储数据到 Elasticsearch 的行为叫做 *索引* （indexing）

关于数据的概念

```
Relational DB -> Databases 数据库 -> Tables 表 -> Rows 行 -> Columns 列
Elasticsearch -> Indices 索引库 -> Types 类型 -> Documents 文档 -> Fields 字段/属性
```

一个 Elasticsearch 集群可以 包含多个 *索引* （indices 数据库），相应的每个索引可以包含多个 *类型*（type 表） 。 这些不同的类型存储着多个 *文档*（document 数据行） ，每个文档又有 多个 *属性* （field 列）。

### 4 Elasticsearch 集群（cluster）

Elasticsearch 尽可能地屏蔽了分布式系统的复杂性。这里列举了一些在后台自动执行的操作：

- 分配文档到不同的容器 或 *分片* 中，文档可以储存在一个或多个节点中
- 按集群节点来均衡分配这些分片，从而对索引和搜索过程进行负载均衡
- 复制每个分片以支持数据冗余，从而防止硬件故障导致的数据丢失
- 将集群中任一节点的请求路由到存有相关数据的节点
- 集群扩容时无缝整合新节点，重新分配分片以便从离群节点恢复

![elas_cluster](./images/elas_cluster.png)

#### 节点（node）

**一个运行中的 Elasticsearch 实例称为一个 节点**，而集群是由一个或者多个拥有相同 `cluster.name` 配置的节点组成， 它们共同承担数据和负载的压力。当有节点加入集群中或者从集群中移除节点时，集群将会重新平均分布所有的数据。

当一个节点被选举成为 ***主* 节点（master）时， 它将负责管理集群范围内的所有变更**，例如增加、删除索引，或者增加、删除节点等。 而**主节点并不需要涉及到文档级别的变更和搜索等操作**，所以当集群只拥有一个主节点的情况下，即使流量的增加它也不会成为瓶颈。 任何节点都可以成为主节点。我们的示例集群就只有一个节点，所以它同时也成为了主节点。

作为用户，**我们可以将请求发送到 *集群中的任何节点* ，包括主节点**。 每个节点都知道任意文档所处的位置，并且能够将我们的请求直接转发到存储我们所需文档的节点。 无论我们将请求发送到哪个节点，它都能负责从各个包含我们所需文档的节点收集回数据，并将最终结果返回給客户端。 Elasticsearch 对这一切的管理都是透明的。

#### 分片（shard）

一个 *分片* 是一个底层的 *工作单元* ，它仅保存了 全部数据中的一部分。

索引实际上是指向一个或者多个物理 *分片* 的 *逻辑命名空间* 。

文档被存储和索引到分片内，但是应用程序是直接与索引而不是与分片进行交互。

Elasticsearch 是利用分片将数据分发到集群内各处的。分片是数据的容器，文档保存在分片内，分片又被分配到集群内的各个节点里。 当你的集群规模扩大或者缩小时， Elasticsearch 会自动的在各节点中迁移分片，使得数据仍然均匀分布在集群里。

##### 主分片（primary shard）

索引内任意一个文档都归属于一个主分片，所以主分片的数目决定着索引能够保存的最大数据量。

##### 复制分片（副分片 replica shard)

一个副本分片只是一个主分片的拷贝。 副本分片作为硬件故障时保护数据不丢失的冗余备份，并为搜索和返回文档等读操作提供服务。

**在索引建立的时候就已经确定了主分片数，但是副本分片数可以随时修改.**

初始设置索引的分片方法

```http
PUT /blogs
{
   "settings" : {
      "number_of_shards" : 3,
      "number_of_replicas" : 1
   }
}
```

* number_of_shards

	每个索引的主分片数，默认值是 `5` 。这个配置在索引创建后不能修改。

* number_of_replicas

	每个主分片的副本数，默认值是 `1` 。对于活动的索引库，这个配置可以随时修改。

2 个节点

![elas_cluster](./images/elas_cluster.png)

3 个节点

![elas_cluster_node3](./images/elas_cluster_node3.png)

分片是一个功能完整的搜索引擎，它拥有使用一个节点上的所有资源的能力。 我们这个拥有6个分片（3个主分片和3个副本分片）的索引可以最大扩容到6个节点，每个节点上存在一个分片，并且每个分片拥有所在节点的全部资源。

修改复制分片数目的方法

```http
PUT /blogs/_settings
{
   "number_of_replicas" : 2
}
```

拥有越多的副本分片时，也将拥有越高的吞吐量。

![elas_0205](./images/elas_0205.png)

#### 故障转移 failover

![elas_0206](./images/elas_0206.png)

- 选举新的主节点
- 提升复制分片为主分片

#### 查看集群健康状态

```http
GET /_cluster/health

{
   "cluster_name":          "elasticsearch",
   "status":                "green", 
   "timed_out":             false,
   "number_of_nodes":       1,
   "number_of_data_nodes":  1,
   "active_primary_shards": 0,
   "active_shards":         0,
   "relocating_shards":     0,
   "initializing_shards":   0,
   "unassigned_shards":     0
}
```

`status` 字段指示着当前集群在总体上是否工作正常。它的三种颜色含义如下：

- `green`

  所有的主分片和副本分片都正常运行。

- `yellow`

  所有的主分片都正常运行，但不是所有的副本分片都正常运行。

- `red`

  有主分片没能正常运行。

### 5 安装中文分析器

<https://github.com/medcl/elasticsearch-analysis-ik>

将elasticsearch-analysis-ik-5.6.16.zip 复制到虚拟机中

```shell
scp elasticsearch-analysis-ik-5.6.16.zip python@10.211.55.7:~/
```

安装

```shell
sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install file:///home/python/elasticsearch-analysis-ik-5.6.16.zip
```

```shell
-> Downloading file:///home/python/elasticsearch-analysis-ik-5.6.16.zip
[=================================================] 100%
-> Installed analysis-ik
```

重新启动

```shell
sudo systemctl restart elasticsearch
```

##### 测试分析器

```http
curl -X GET 127.0.0.1:9200/_analyze?pretty -d '
{
  "analyzer": "standard",
  "text": "我是&中国人"
}'

curl -X GET 127.0.0.1:9200/_analyze?pretty -d '
{
  "analyzer": "ik_max_word",
  "text": "我是&中国人"
}'
```

### 6 索引

##### 创建索引

索引可以在添加文档数据时，通过动态映射的方式自动生成索引与类型。

索引也可以手动创建，通过手动创建，可以控制主分片数目、分析器和类型映射。

```http
PUT /my_index
{
    "settings": { ... any settings ... },
    "mappings": {
        "type_one": { ... any mappings ... },
        "type_two": { ... any mappings ... },
        ...
    }
}

curl 127.0.0.1:9200/articles?pretty
```

**注： 在Elasticsearch 5.x版本中，设置分片与设置索引的类型字段需要分两次设置完成。**

##### 删除索引

用以下的请求来 删除索引:

```http
DELETE /my_index
```

你也可以这样删除多个索引：

```http
DELETE /index_one,index_two
DELETE /index_*
```

你甚至可以这样删除 *全部* 索引：

```http
DELETE /_all
DELETE /*
```

创建文章索引

```http
// 文章索引
curl -X PUT 127.0.0.1:9200/articles -H 'Content-Type: application/json' -d'
{
   "settings" : {
   		"index": {
          "number_of_shards" : 3,
      		"number_of_replicas" : 1
   		}
   }
}
'
```

### 7 类型和映射

*类型* 在 Elasticsearch 中表示一类相似的文档，类型由 *名称* 和 *映射* （ mapping）组成。

*映射*, mapping， 就像数据库中的 schema ，描述了文档可能具有的字段或 *属性* 、 每个字段的数据类型—比如 `string`, `integer` 或 `date`。

为了能够将时间字段视为时间，数字字段视为数字，字符串字段视为全文或精确值字符串， Elasticsearch 需要知道每个字段中数据的类型。

简单字段类型：

- 字符串: `text`      (es2.x  string)
- 整数 : `byte`, `short`, `integer`, `long`
- 浮点数: `float`, `double`
- 布尔型: `boolean`
- 日期: `date`

自定义类型映射， 以头条项目文章为例   python

```http
curl -X PUT 127.0.0.1:9200/articles/_mapping/article -H 'Content-Type: application/json' -d'
{
           "_all": {
                "analyzer": "ik_max_word",
                "search_analyzer": "ik_max_word",
                "term_vector": "no",
                "store": "false"
            },
            "properties": {
                "article_id": {
                    "type": "long",
                    "store": "false",
                    "include_in_all": "false"
                },
                "user_id": {
                  	"type": "long",
                    "store": "false",
                    "include_in_all": "false"
                },
                "title": {
                    "type": "text",
                    "store": "false",
                    "term_vector": "with_positions_offsets",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "include_in_all": "true",
                    "boost": 2
                },
                "content": {
                    "type": "text",
                    "store": "false",
                    "term_vector": "with_positions_offsets",
                    "analyzer": "ik_max_word",
                    "include_in_all": "true"
                },
                "status": {
                    "type": "byte",
                    "store": "false",
                    "include_in_all": "false"
                },
                "create_time": {
                    "type": "date",
                    "store": "false",
                    "include_in_all": "false"
                }
            }

}
'
```

查看映射

```http
curl 127.0.0.1:9200/articles/_mapping/article?pretty
```

#### 映射修改

一个类型映射创建好后，可以为类型增加新的字段映射

```http
curl -X PUT 127.0.0.1:9200/articles/_mapping/article -H 'Content-Type:application/json' -d '
{
  "properties": {
    "new_tag": {
      "type": "text"
    }
  }
}
'
```

**但是不能修改已有字段的类型映射，原因在于elasticsearch已按照原有字段映射生成了反向索引数据，类型映射改变意味着需要重新构建反向索引数据，所以并不能再原有基础上修改，只能新建索引库，然后创建类型映射后重新构建反向索引数据。**

```http
curl -X PUT 127.0.0.1:9200/articles_v2 -H 'Content-Type: application/json' -d'
{
   "settings" : {
   		"index": {
          "number_of_shards" : 3,
      		"number_of_replicas" : 1
   		}
   }
}
'

curl -X PUT 127.0.0.1:9200/articles_v2/_mapping/article -H 'Content-Type: application/json' -d'
{
           "_all": {
                "analyzer": "ik_max_word",
                "search_analyzer": "ik_max_word",
                "term_vector": "no",
                "store": "false"
            },
            "properties": {
                "article_id": {
                    "type": "long",
                    "store": "false",
                    "include_in_all": "false"
                },
                "user_id": {
                  	"type": "long",
                    "store": "false",
                    "include_in_all": "false"
                },
                "title": {
                    "type": "text",
                    "store": "false",
                    "term_vector": "with_positions_offsets",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word",
                    "include_in_all": "true",
                    "boost": 2
                },
                "content": {
                    "type": "text",
                    "store": "false",
                    "term_vector": "with_positions_offsets",
                    "analyzer": "ik_max_word",
                    "include_in_all": "true"
                },
                "status": {
                    "type": "byte",
                    "store": "false",
                    "include_in_all": "false"
                },
                "create_time": {
                    "type": "date",
                    "store": "false",
                    "include_in_all": "false"
                }
            }

}
'
```

##### 重新索引数据

```http
curl -X POST 127.0.0.1:9200/_reindex -H 'Content-Type:application/json' -d '
{
  "source": {
    "index": "articles"
  },
  "dest": {
    "index": "articles_v2"
  }
}
'
```

##### 为索引起别名

为索引起别名，让新建的索引具有原索引的名字，可以让应用程序零停机。

```http
curl -X DELETE 127.0.0.1:9200/articles
curl -X PUT 127.0.0.1:9200/articles_v2/_alias/articles
```

查询索引别名

```http
# 查看别名指向哪个索引
curl 127.0.0.1:9200/*/_alias/articles

# 查看哪些别名指向这个索引
curl 127.0.0.1:9200/articles_v2/_alias/*
```

```http
PUT  /articles_v1
PUT  /articles_v1/_alias/articles

PUT  /articles_v2
PUT  /articles_v2/_alias/articles
```

### 8 文档

```json
{
    "name":         "John Smith",
    "age":          42,
    "confirmed":    true,
    "join_date":    "2014-06-01",
    "home": {
        "lat":      51.5,
        "lon":      0.1
    },
    "accounts": [
        {
            "type": "facebook",
            "id":   "johnsmith"
        },
        {
            "type": "twitter",
            "id":   "johnsmith"
        }
    ]
}
```

一个文档不仅仅包含它的数据 ，也包含 *元数据*(metadata) —— *有关* 文档的信息。 三个必须的元数据元素如下：

- `_index`

  文档在哪存放

- `_type`

  文档表示的对象类别

- `_id`

  文档唯一标识

#####  索引文档（保存文档数据）

使用自定义的文档id

```http
PUT /{index}/{type}/{id}
{
  "field": "value",
  ...
}
```

```http
curl -X PUT 127.0.0.1:9200/articles/article/150000 -H 'Content-Type:application/json' -d '
{
  "article_id": 150000,
  "user_id": 1,
  "title": "python是世界上最好的语言",
  "content": "确实如此",
  "status": 2,
  "create_time": "2019-04-03"
}'
```

_version 每次修改文档数据，版本都会增加，可以当作乐观锁的依赖（判断标准）使用

自动生成文档id

```http
PUT /{index}/{type}
{
  "field": "value",
  ...
}
```

##### 获取指定文档

```http
curl 127.0.0.1:9200/articles/article/150000?pretty

# 获取一部分
curl 127.0.0.1:9200/articles/article/150000?_source=title,content
curl 127.0.0.1:9200/articles/article/150000?_source
```

##### 判断文档是否存在

```http
curl -i -X HEAD 127.0.0.1:9200/articles/article/150000
```

* 存在 200状态码
* 不存在 404状态码

##### 更新文档

在 Elasticsearch 中文档是 *不可改变* 的，不能修改它们。 相反，如果想要更新现有的文档，需要 *重建索引*或者进行替换。我们可以使用相同的 `index` API 进行实现。

```http
curl -X PUT 127.0.0.1:9200/articles/article/150000 -H 'Content-Type:application/json' -d '
{
  "article_id": 150000,
  "user_id": 1,
  "title": "python必须是世界上最好的语言",
  "content": "确实如此",
  "status": 2,
  "create_time": "2019-04-03"
}'
```

注意返回值_version的变化

##### 删除文档

```http
curl -X DELETE 127.0.0.1:9200/articles/article/150000
```

##### 取回多个文档

```http
curl -X GET 127.0.0.1:9200/_mget -d '
{
  "docs": [
    {
      "_index": "articles",
      "_type": "article",
      "_id": 150000
    },
    {
      "_index": "articles",
      "_type": "article",
      "_id": 150001
    }
  ]
}'
```

##### 批量设置操作

```js
POST /_bulk
{ "delete": { "_index": "website", "_type": "blog", "_id": "123" }} 
{ "create": { "_index": "website", "_type": "blog", "_id": "123" }}
{ "title":    "My first blog post" }
{ "index":  { "_index": "website", "_type": "blog" }}
{ "title":    "My second blog post" }
{ "update": { "_index": "website", "_type": "blog", "_id": "123", "_retry_on_conflict" : 3} }
{ "doc" : {"title" : "My updated blog post"} }
```

### 9 Logstash导入数据

使用logstash 导入工具从mysql中导入数据

##### Logstach安装

```shell
sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
```

在 /etc/yum.repos.d/ 中创建logstash.repo文件

```
[logstash-6.x]
name=Elastic repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```

执行

```shell
sudo yum install logstash
```

```shell
cd /usr/share/logstash/bin/
sudo ./logstash-plugin install logstash-input-jdbc
sudo ./logstash-plugin install logstash-output-elasticsearch
scp mysql-connector-java-8.0.13.tar.gz python@10.211.55.7:~/
tar -zxvf mysql-connector-java-8.0.13.tar.gz
```

配置文件

```
input{
     jdbc {
         jdbc_driver_library => "/home/python/mysql-connector-java-8.0.13/mysql-connector-java-8.0.13.jar"
         jdbc_driver_class => "com.mysql.jdbc.Driver"
         jdbc_connection_string => "jdbc:mysql://127.0.0.1:3306/toutiao?tinyInt1isBit=false"
         jdbc_user => "root"
         jdbc_password => "mysql"
         jdbc_paging_enabled => "true"
         jdbc_page_size => "1000"
         jdbc_default_timezone =>"Asia/Shanghai"
         statement => "select a.article_id as article_id,a.user_id as user_id, a.title as title, a.status as status, a.create_time as create_time,  b.content as content from news_article_basic as a inner join news_article_content as b on a.article_id=b.article_id"
         use_column_value => "true"
         tracking_column => "article_id"
         clean_run => true
     }
}
output{
      elasticsearch {
         hosts => "127.0.0.1:9200"
         index => "articles"
         document_id => "%{article_id}"
         document_type => "article"
      }
      stdout {
         codec => json_lines
     }
}
```

```shell
sudo /usr/share/logstash/bin/logstash -f ./logstash_mysql.conf
```

### 10 查询

```http
GET /megacorp/employee/1
GET /megacorp/employee/_search
GET /megacorp/employee/_search?q=last_name:Smith

GET /megacorp/employee/_search
{
    "query" : {
        "match" : {
            "last_name" : "Smith"
        }
    }
}

curl -X GET 127.0.0.1:9200/articles/article/_search?pretty -d '
{
		"from": 0,
		"size": 5,
		"_source": ["title"],
    "query": {
        "match": {
           "title": "python"
         }
     }
}'

GET /megacorp/employee/_search
{
    "query" : {
        "bool": {
            "must": {
                "match" : {
                    "last_name" : "smith" 
                }
            },
            "filter": {
                "range" : {
                    "age" : { "gt" : 30 } 
                }
            }
        }
    }
}

curl -X GET 127.0.0.1:9200/articles/article/_search?pretty -d '
{
	"_source": ["title", "status"],
  "query": {
    "bool": {
      "must": {
        "match": {
          "title": "python"
        }
      },
      "filter": {
        "term": {
          "status": {
            "value": 2
          }
        }
      }
    }
  }
}
'

curl -X GET 127.0.0.1:9200/articles/article/_search?pretty -d '
{
	"_source": ["title"],
  "query": {
    "match": {
      "_all": "python web 编程"
    }
  }
}
'



# 全文检索
GET /megacorp/employee/_search
{
    "query" : {
        "match" : {
            "about" : "rock climbing"
        }
    }
}

# 短语搜索
GET /megacorp/employee/_search
{
    "query" : {
        "match_phrase" : {
            "about" : "rock climbing"
        }
    }
}

curl -X GET 127.0.0.1:9200/articles/article/_search?pretty -d '
{
	"_source": ["title"],
  "query": {
    "match_phrase": {
      "_all": "python web 编程"
    }
  }
}
'

# 高亮搜索
GET /megacorp/employee/_search
{
    "query" : {
        "match_phrase" : {
            "about" : "rock climbing"
        }
    },
    "highlight": {
        "fields" : {
            "about" : {}
        }
    }
}

curl -X GET 127.0.0.1:9200/articles/article/_search?pretty -d '
{
	"size":1,
  "query": {
    "match": {
      "title": "python web 编程"
    }
  },
  "highlight":{
    "fields": {
      "title": {}
    }
  }
}
'



# 聚合（分析）
GET /megacorp/employee/_search
{
    "aggs" : {
        "all_interests" : {
            "terms" : { "field" : "interests" },
            "aggs" : {
                "avg_age" : {
                    "avg" : { "field" : "age" }
                }
            }
        }
    }
}

# 分页
GET /_search?size=5
GET /_search?size=5&from=5
GET /_search?size=5&from=10


curl -X GET 127.0.0.1:9200/articles/article/_search -d '
{
	 "from": 0,
	 "size": 10,
	 "_source": ["article_id", "title"],
   "query": {
        "match": {
             "title": "python"
        }
    }
}'
```

组合查询

* must

文档 *必须* 匹配这些条件才能被包含进来。

* must_not

文档 *必须不* 匹配这些条件才能被包含进来。

* should

如果满足这些语句中的任意语句，将增加 `_score` ，否则，无任何影响。它们主要用于修正每个文档的相关性得分。

* filter

*必须* 匹配，但它以不评分、过滤模式来进行。这些语句对评分没有贡献，只是根据过滤标准来排除或包含文档。

```json
{
    "bool": {
        "must":     { "match": { "title": "how to make millions" }},
        "must_not": { "match": { "tag":   "spam" }},
        "should": [
            { "match": { "tag": "starred" }}
        ],
        "filter": {
          "range": { "date": { "gte": "2014-01-01" }} 
        }
    }
}
```

* term 精确查找
* range 范围查找
* match 全文检索
* boost 增加权重

##### 排序

```http
GET /_search
{
    "query" : {
        "bool" : {
            "filter" : { "term" : { "user_id" : 1 }}
        }
    },
    "sort": { "date": { "order": "desc" }}
}

GET /_search
{
    "query" : {
        "bool" : {
            "must":   { "match": { "tweet": "manage text search" }},
            "filter" : { "term" : { "user_id" : 2 }}
        }
    },
    "sort": [
        { "date":   { "order": "desc" }},
        { "_score": { "order": "desc" }}
    ]
}
```

### 11 Python客户端

<https://elasticsearch-py.readthedocs.io/en/master/>

```shell
pip install elasticsearch
```

```python
from elasticsearch5 import Elasticsearch

ES = [
        '172.17.0.135:9200'
    ]

es = Elasticsearch(
        ES,
        # sniff before doing anything
        sniff_on_start=True,
        # refresh nodes after a node fails to respond
        sniff_on_connection_fail=True,
        # and also every 60 seconds
        sniffer_timeout=60
    )


query = {
            'from': (page-1)*per_page,
            'size': per_page,
            '_source': False,
            'query': {
                'bool': {
                    'must': [
                        {'match': {'_all': q}}
                    ],
                    'filter': [
                        {'term': {'status': {'value': 2}}}
                    ]
                }
            }
        }
ret = current_app.es.search(index='articles', doc_type='article', body=query)
```

### 12 自动补全  联想

```http
// 搜索词补全
curl -X PUT 127.0.0.1:9200/completions -H 'Content-Type: application/json' -d'
{
   "settings" : {
   		"index": {
            "number_of_shards" : 3,
      		"number_of_replicas" : 1
   		}
   }
}
'


```

```http
curl -X PUT 127.0.0.1:9200/completions/_mapping/words -H 'Content-Type: application/json' -d'
{
       "words": {
            "properties": {
                "suggest": {
                    "type": "completion",
                    "analyzer": "ik_max_word",
                    "search_analyzer": "ik_max_word"
                }
            }
       }
}
'


input{
     jdbc {
         jdbc_driver_library => "/home/python/mysql-connector-java-8.0.13/mysql-connector-java-8.0.13.jar"
         jdbc_driver_class => "com.mysql.jdbc.Driver"
         jdbc_connection_string => "jdbc:mysql://127.0.0.1:3306/toutiao?tinyInt1isBit=false"
         jdbc_user => "root"
         jdbc_password => "mysql"
         jdbc_paging_enabled => "true"
         jdbc_page_size => "1000"
         jdbc_default_timezone =>"Asia/Shanghai"
         statement => "select title as suggest from news_article_basic"
         clean_run => true
     }
}
output{
      elasticsearch {
         hosts => "127.0.0.1:9200"
         index => "completions"
         document_type => "words"
      }
}
```

```http
curl 127.0.0.1:9200/completions/words/_search?pretty -d '
{
    "suggest": {
        "title-suggest" : {
            "prefix" : "pyth", 
            "completion" : { 
                "field" : "suggest" 
            }
        }
    }
}
'
```

<https://blog.csdn.net/wwd0501/article/details/80595201>

ELK