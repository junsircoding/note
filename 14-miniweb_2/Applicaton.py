#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 14-miniweb_2/Applicaton.py
# @Info        : 
# @Last Edited : 2022-06-14 22:22:27

import json

import pymysql

route_list = []


def router(path):
    def decorator(action):
        route_list.append((path, action))

        def inner():
            pass

    return decorator


@router('/index.html')
def index():
    # 连接数据库，参数有6个host=None, user=None, password="",database=None, port=0, unix_socket=None,charset=''
    conn = pymysql.connect(host='localhost', user='root', password='mysql', database='miniweb', port=3306,
                           charset='utf8')
    # 获取游标
    cur = conn.cursor()
    # 写sql语句
    sql = 'SELECT * FROM user'
    # 用游标执行sql
    cur.execute(sql)
    # 用游标获取执行结果，返回元组组成的列表
    sql_data = cur.fetchall()
    # 打开网页文件，将模板变量替换为查询结果
    with open('static/index.html', 'r') as f:
        template = f.read()
    isReplaced = ''
    for i in sql_data:
        isReplaced += """<tr>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                         </tr>""" % i
    template = template.replace('<%content%>', isReplaced)
    # 用连接对象提交，若只是查询可省略这一步
    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()
    return template


@router('/hobby.html')
def hobby():
    with open('static/hobby.html', 'r') as f:
        template = f.read()
    return template


@router('/hobby_info.html')
def hobby_info():
    # 连接数据库，参数有6个host=None, user=None, password="",database=None, port=0, unix_socket=None,charset=''
    conn = pymysql.connect(host='localhost', user='root', password='mysql', database='miniweb', port=3306,
                           charset='utf8')
    # 获取游标
    cur = conn.cursor()
    # 写sql语句
    sql = 'SELECT u.usernmae, u.phone, u.birth, i.hobby FROM user as u INNER JOIN info as i on u.id = i.userid'
    # 用游标执行sql
    cur.execute(sql)
    # 用游标获取执行结果，返回元组组成的列表
    sql_data = cur.fetchall()
    # 用连接对象提交，若只是查询可省略这一步
    # 构造大列表
    json_list = list()
    for sql_line in sql_data:
        # 构造大列表中的小字典
        json_dict = dict()
        json_dict['username'] = sql_line[0]
        json_dict['phone'] = sql_line[1]
        json_dict['birth'] = sql_line[2]
        json_dict['hobby'] = sql_line[3]
        json_list.append(json_dict)

    template = json.dumps(json_list, ensure_ascii=False)
    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()

    # 返回json数据
    return template

def app(source_action):
    file_name = source_action['file_name']
    # 遍历路由表，找到要请求的action，返回响应体，最后构造响应报文
    for url, response_body in route_list:
        if url == file_name:
            return response_body()
