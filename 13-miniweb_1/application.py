#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 13-miniweb_1/application.py
# @Info        : 
# @Last Edited : 2022-06-08 18:04:57

import pymysql


# 视图函数
# 主页
def index():
    with open('static/index.html', 'r') as f:
        data = f.read()
    # 连接数据库
    conn = pymysql.connect(host='localhost', user='root', password='mysql',
                           database='miniweb', port=3306, charset='utf8')
    # 获取游标
    cur = conn.cursor()
    # 写sql语句
    sql = 'SELECT * FROM user'
    # 用游标执行sql
    cur.execute(sql)
    # 获取查询结果
    search_res = cur.fetchall()

    # 遍历查询结果，编写响应报文
    response_body = ''
    for i in search_res:
        response_body += """<tr><td>%s</td><td>%s</td><td>%s</td>
            <td>%s</td><td>%s</td><td>%s</td></tr>""" % i

    data = data.replace('<%content%>', response_body)
    # 用连接对象提交sql(只查询不用提交)
    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()
    return data


# 爱好
def hobby():
    with open('static/hobby.html', 'r') as f:
        data = f.read()
    # 连接数据库
    conn = pymysql.connect(host='localhost', user='root', password='mysql',
                           database='miniweb', port=3306, charset='utf8')
    # 获取游标
    cur = conn.cursor()
    # 写sql语句
    sql = 'SELECT * FROM info'
    # 用游标执行sql
    cur.execute(sql)
    # 获取查询结果
    search_res = cur.fetchall()
    # 遍历查询结果，编写响应报文
    response_body = ''
    for i in search_res:
        response_body += """<tr><td>%s</td><td>%s</td><td>%s</td>
        </tr>""" % i

    data = data.replace('<%content%>', response_body)
    # 用连接对象提交sql(只查询不用提交)
    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()
    return data


# 编写路由表
route_list = [
    ('index.html', index()),
    ('hobby.html', hobby())
]


def app(env):
    file_name = env['file_name']
    file_name = file_name.replace('/', '')
    for url, func in route_list:
        if url == file_name:
            return func
        else:
            print('error')
