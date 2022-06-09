#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 03-ElasticSearch/Elasticsearch客户端.py
# @Info        : 
# @Last Edited : 2022-06-09 14:57:29

"""
Elasticsearch 客户端
"""
import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch import helpers
# 导入自定义 logger
logger = ""

es_config = {
    "dev": [],
    "stg": [],
    "prd": []
}


class EsService(object):
    """ES 服务"""

    def __init__(self, env):
        """"""
        self.env = env
        self.hosts = es_config.get(self.env)
        self.es = Elasticsearch(self.hosts)

    def exists(self, index_name):
        """索引存在判断
        Args:
            index_name(str): 索引名称
        Returns:
            (bool): 是否存在
        """
        if self.es.indices.exists(index=index_name) is True:
            return True
        else:
            return False

    def delete(self, index_name):
        """删除索引
        Args:
            index_name(str): 索引名称
        Returns:
            (bool): 是否存在
        """
        if self.es.indices.exists(index=index_name) is True:
            self.es.indices.delete(index_name, ignore=[400, 404])
            logger.info(f"ES 索引 {index_name} 删除成功")
            return True
        else:
            logger.info(f"ES 索引 {index_name} 不存在, 无须删除")
            return False

    def create(self, index_name, field_body):
        """创建索引
        Args:
            index_name(str): 索引名称
            field_body(dict): body 传入需要构建的表格字段参数
            参考:
            field_body = {
                "properties": {
                    "query": {
                        "type": "text",
                        "analyzer": "dl_smart",
                        "search_analyzer": "dl_smart"
                    },
                    "title": {"type": "keyword"},
                    "id": {"type": "keyword"}
                }
            }
            """
        # 创建映射
        body = {
            "mappings": {index_name: field_body}
        }
        if self.es.indices.exists(index=index_name) is not True:
            try:
                res = self.es.indices.create(index=index_name, body=body)
            except:
                for field, properties in field_body["properties"].items():
                    if "analyzer" in properties:
                        if "dl" in properties:
                            old_analyzer = body["mappings"][index_name]["properties"][field]["analyzer"]
                            new_analyzer = old_analyzer.replace("dl", "ik")
                            body["mappings"][index_name]["properties"][field]["analyzer"] = new_analyzer
                            logger.info(f"ES 定义字段 {field} 的 analyzer 时, 没有分析器 {old_analyzer}, 替换为 {new_analyzer}")
                    if "search_analyzer" in properties:
                        if "dl" in properties.get("search_analyzer"):
                            old_search_analyzer = body["mappings"][index_name]["properties"][field]["search_analyzer"]
                            new_search_analyzer = old_search_analyzer.replace("dl", "ik")
                            body["mappings"][index_name]["properties"][field]["search_analyzer"] = new_search_analyzer
                            logger.info(f"ES 定义字段 {field} 的 search_analyzer 时, 没有分析器 {old_search_analyzer}, 替换为 {new_search_analyzer}")
                res = self.es.indices.create(index=index_name, body=body)
            logger.info(f"ES 中不存在索引 {index_name}, 新建成功")



    def upload(self, index_name, data: pd.DataFrame, id_name):
        """新增数据
        Args:
            index_name(str): 索引名称
            data(pd.DataFrame): 数据
            id_name(str): id 列列名"""
        actions = []
        cols = data.columns
        for row in data.iterrows():
            action = {
                "_index": index_name,
                "_type": index_name,
                "_id": row[1][id_name],
                "_source": {
                    col: row[1][col] for col in cols
                }
            }

            actions.append(action)
            if (len(actions)==500):
                helpers.bulk(self.es, actions)
                del actions[0:len(actions)]
        
        if (len(actions) > 0):
            helpers.bulk(self.es, actions)
        logger.info(f"ES 索引 {index_name} 导入数据成功, 字段数: {data.shape[1]}, 数据量: {data.shape[0]}")


    def remove(self, index_name, field, values):
        """删除数据
        Args:
            index_name(str): 索引名称
            field(str): 字段名
            values(list): 删除的值
        Returns:
        """
        query = {
            "query": {
                "term": {field: values}
            }
        }
        self.es.delete_by_query(index=index_name, body=query, doc_type=index_name)
        logger.info(f"ES 索引 {index_name} 删除 {field} 字段的 {values} 成功")

    def search(self, index_name, field, value, count, search_type="match", keep_source=False):
        """搜索
        Args:
            index_name(str): 索引名称
            field(list): 搜索的字段
            value(str): 搜索值
            count(int): 返回结果数量
            search_type(str): 查询类型, 可选 match, term, match_phrase 默认 match
            keep_source(bool): 只保留 _source 字段, 默认为 True
        Returns:

        """
        if search_type == "term":
            body = {
                "query": {
                    "term": {field: value}
                }
            }
        elif search_type == "match_phrase":
            body = {
                "query": {
                    "match_phrase": {field: value}
                }
            }
        else:
            body = {
                "query": {
                    "match": {field: value}
                }
            }
        es_data = self.es.search(index=index_name, body=body, size=count)
        if not es_data["hits"]["hits"]:
            res = []
        else:
            if keep_source:
                res = [item["_source"] for item in es_data["hits"]["hits"]]
            else:
                res = [item for item in es_data["hits"]["hits"]]
        return res

    def get_all_data(self, index_name, keep_fields=None):
        """获取所有数据
        Args:
            index_name(str): 索引名称
            keeo_fields(list): 字段名称
        Returns:
            (pd.DataFrame): 数据
        """
        body = {
            "query": {
                "match_all": {}  # 匹配所有文档
            },
            "size": 10000
        }
        if keep_fields:
            body["_source"] = keep_fields
        # 滚动取数先取前 1W
        query_data = self.es.search(
            index=index_name, scroll="5m", timeout="3s", size=10000, body=body)
        mdata = query_data.get("hits").get("hits")
        if not mdata:
            logger.warning(f"ES 索引 {index_name} 无数据")
        scroll_id = query_data["_scroll_id"]
        total = query_data["hits"]["hits"]

        # 滚动取 1W 之后的数据
        for i in range(total // 10000):
            # scroll_id 决定了要从哪里开始滚动拿数据(scroll_id 不需要根据每次取数改变), scroll 参数必须制定否则会报错
            res = self.es.scroll(scroll_id=scroll_id, scroll="5m")
            mdata += res.get("hits").get("hits")

        # 取数结果转 DataFrame
        lk = []
        for i in mdata:
            lk.append(i["_source"])
        result = pd.DataFrame(lk)
        data_shape = result.shape
        logger.warning(f"ES 索引 {index_name} 取全量数据完成: {data_shape}")
        return result

    def analyce(self, text, analyzer):
        """分析, 即 ElasticSearch 分析器对文本的分析(分词、过滤、处理)
        Args:
            text(str): 分析文本
            analyzer(str): 分析器
        Returns:
            (dict): 分析结果
        """
        body = {
            "text": text,
            "analyzer": analyzer
        }
        analyzer_result = self.es.indices.analyze(body=body)
        return analyzer_result

    def get_all_index(self, str):
        """获取所有索引
        Args:
            str(str): 索引名称或部分名称
        Returns:
            (dict): 索引查询结果
        """
        index_result = self.es.indices.get_alias(str)
        return index_result
