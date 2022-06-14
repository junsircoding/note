#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 13-miniweb_1/createdata.py
# @Info        : 
# @Last Edited : 2022-06-14 22:22:27

# 创建MiniWeb项目第一步：创建数据库
# 用pymysql方式导入数据
# 导入pymysql包
import pymysql

# 创建连接
# host=None, user=None, password="",database=None, port=0,charset=''
conn = pymysql.connect(host='localhost', user='root', password='mysql',
                       database='miniweb', port=3306, charset='utf8')
# 获取游标
cur = conn.cursor()
# 读取data.txt的数据
with open('info.txt', 'r', encoding='UTF-8') as f:
    data = f.readlines()
for data_line in data:
    line_list = data_line.split(':')
    # sql = 'INSERT INTO user VALUES (0, %s, %s, %s, %s, %s)'
    sql = 'INSERT INTO info VALUES (0, %s, %s)'
    # 用游标执行sql语句
    cur.execute(sql, line_list)
# 用连接对象向数据库提交查询
conn.commit()
# 关闭游标
cur.close()
# 关闭连接
conn.close()
