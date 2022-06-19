#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 01-Scripts/05-自定义Flask日志格式.py
# @Info        : 
# @Last Edited : 2022-06-19 21:07:34

"""
自定义 Flask 日志格式
"""

import logging

from flask import Flask, request
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
# 设置是否传递异常 , 如果为 True, 则 flask 运行中的错误会显示到网页中, 如果为 False, 则会输出到文件中
app.config['PROPAGATE_EXCEPTIONS'] = False


class RequestFormatter(logging.Formatter):  # 自定义格式化类
    def format(self, record):
        """每次生成日志时都会调用, 该方法主要用于设置自定义的日志信息
        :param record 日志信息"""
        record.url = request.url  # 获取请求的url
        record.remote_addr = request.remote_addr  # 获取客户端的ip

        return super().format(record)  # 执行父类的默认操作

"""
flask中提供了两个日志
1> werkzeug 记录 web 应用运行中出现的错误
2> flask.app  给开发者预留的日志
flask 中的运行错误也会记录到 flask.app 的日志中
"""
def create_logger():
    """
    配置 flask日志
    """
    # 创建flask.app日志器
    flask_logger = logging.getLogger('flask.app')
    # 设置全局级别
    flask_logger.setLevel('DEBUG')

    # 创建控制台处理器
    console_handler = logging.StreamHandler()

    # 给处理器设置输出格式
    console_formatter = logging.Formatter(
        fmt='%(name)s %(levelname)s %(pathname)s %(lineno)d %(message)s')
    console_handler.setFormatter(console_formatter)

    # 日志器添加处理器
    flask_logger.addHandler(console_handler)

    # 创建文件处理器
    # 转存文件处理器  当达到限定的文件大小时, 可以将日志转存到其他文件中
    file_handler = RotatingFileHandler(
        filename='flask.log', maxBytes=100 * 1024 * 1024, backupCount=10)

    # 给处理器设置输出格式
    file_formatter = RequestFormatter(
        fmt='[%(asctime)s] %(remote_addr)s requested %(url)s %(name)s %(levelname)s %(pathname)s %(lineno)d %(message)s')
    file_handler.setFormatter(file_formatter)
    # 单独设置文件处理器的日志级别
    file_handler.setLevel('WARN')

    # 日志器添加处理器
    flask_logger.addHandler(file_handler)


@app.route('/')
def index():
    num = 1 / 0
    app.logger.error('this is a error')
    return "index"


if __name__ == '__main__':
    create_logger()
    app.run(debug=True)
