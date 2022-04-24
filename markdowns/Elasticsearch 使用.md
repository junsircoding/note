Elasticsearch 练习笔记

[Miniconda 安装包](https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh)
[Jdk 安装包](https://mirrors.huaweicloud.com/java/jdk/8u191-b12/)
[Elasticsearch 安装包](https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.5.1.zip)
[阮一峰教程](https://www.ruanyifeng.com/blog/2017/08/elasticsearch.html)

ES 数据结构图
![](https://p.qlogo.cn/qqmail_head/rwzOcu9uLseNKBm3MFXahbicUMCaTibSiaBsmeWYDLEqTjvDqFZ3HATr8vjN7qgfa29pMycSzgPqYY/0)

查看 ES 服务信息：
```shell
curl localhost:9200
```

查看当前节点所有 Index：
```shell
curl -X GET 'http://localhost:9200/_cat/indices?v'
```

列出每个 Index 所包含的 Type：
```shell
curl 'localhost:9200/_mapping?pretty=true'
```

新建 Index：
```shell
curl -X PUT 'localhost:9200/weather'
{
  "acknowledged":true,
  "shards_acknowledged":true
}
```

删除 Index：
```shell
curl -X DELETE 'localhost:9200/weather'
```

新建 Index，指定需要分词的字段：
```shell
curl -X PUT 'localhost:9200/accounts' -d '
{
  "mappings": {
    "person": {
      "properties": {
        "user": {
          "type": "text",
          "analyzer": "ik_max_word",
          "search_analyzer": "ik_max_word"
        },
        "title": {
          "type": "text",
          "analyzer": "ik_max_word",
          "search_analyzer": "ik_max_word"
        },
        "desc": {
          "type": "text",
          "analyzer": "ik_max_word",
          "search_analyzer": "ik_max_word"
        }
      }
    }
  }
}'
```

新增记录：
```shell
curl -X PUT 'localhost:9200/accounts/person/1' -d '
{
  "user": "张三",
  "title": "工程师",
  "desc": "数据库管理"
}' 
{
  "_index":"accounts",
  "_type":"person",
  "_id":"1",
  "_version":1,
  "result":"created",
  "_shards":{"total":2,"successful":1,"failed":0},
  "created":true
}
```

新增记录：
```shell
curl -X POST 'localhost:9200/accounts/person' -d '
{
  "user": "李四",
  "title": "工程师",
  "desc": "系统管理"
}'
{
  "_index":"accounts",
  "_type":"person",
  "_id":"AV3qGfrC6jMbsbXb6k1p",
  "_version":1,
  "result":"created",
  "_shards":{"total":2,"successful":1,"failed":0},
  "created":true
}
```

查看记录：
```shell
curl 'localhost:9200/accounts/person/1?pretty=true'
{
  "_index" : "accounts",
  "_type" : "person",
  "_id" : "1",
  "_version" : 1,
  "found" : true,
  "_source" : {
    "user" : "张三",
    "title" : "工程师",
    "desc" : "数据库管理"
  }
}
```

删除记录
```shell
curl -X DELETE 'localhost:9200/accounts/person/1'
```

更新记录
```shell
curl -X PUT 'localhost:9200/accounts/person/1' -d '
{
    "user" : "张三",
    "title" : "工程师",
    "desc" : "数据库管理，软件开发"
}' 

{
  "_index":"accounts",
  "_type":"person",
  "_id":"1",
  "_version":2,
  "result":"updated",
  "_shards":{"total":2,"successful":1,"failed":0},
  "created":false
}
```

返回所有记录
```shell
curl 'localhost:9200/accounts/person/_search'
{
  "took":2,
  "timed_out":false,
  "_shards":{"total":5,"successful":5,"failed":0},
  "hits":{
    "total":2,
    "max_score":1.0,
    "hits":[
      {
        "_index":"accounts",
        "_type":"person",
        "_id":"AV3qGfrC6jMbsbXb6k1p",
        "_score":1.0,
        "_source": {
          "user": "李四",
          "title": "工程师",
          "desc": "系统管理"
        }
      },
      {
        "_index":"accounts",
        "_type":"person",
        "_id":"1",
        "_score":1.0,
        "_source": {
          "user" : "张三",
          "title" : "工程师",
          "desc" : "数据库管理，软件开发"
        }
      }
    ]
  }
}
```

全文搜索
```shell
curl 'localhost:9200/accounts/person/_search'  -d '
{
  "query" : { "match" : { "desc" : "软件" }}
}'
```

分页搜索
```shell
curl 'localhost:9200/accounts/person/_search'  -d '
{
  "query" : { "match" : { "desc" : "管理" }},
  "size": 1
}'
```

指定页码
```shell
curl 'localhost:9200/accounts/person/_search'  -d '
{
  "query" : { "match" : { "desc" : "管理" }},
  "from": 1,
  "size": 1
}'
```

OR 搜索
```shell
curl 'localhost:9200/accounts/person/_search'  -d '
{
  "query" : { "match" : { "desc" : "软件 系统" }}
}'
```

AND 搜索
```shell
curl 'localhost:9200/accounts/person/_search'  -d '
{
  "query": {
    "bool": {
      "must": [
        { "match": { "desc": "软件" } },
        { "match": { "desc": "系统" } }
      ]
    }
  }
}'
```   

----

接口调用 Kibana 客户端

http://ip/api/console/proxy?path=index_name%2F_search&method=POST

```python
headers = {
    "Authorization": "Basic a2liYW5hOnByZEAyMDIxMDQ5",
    "kbn-version": "6.5.0"
}
```
