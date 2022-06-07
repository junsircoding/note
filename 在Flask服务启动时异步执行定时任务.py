#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : 在Flask服务启动时异步执行定时任务.py
# @Info        : 
# @Last Edited : 2022-06-07 10:59:16

"""
在 flask 服务启动时异步执行定时任务
"""

# 1. flask 服务
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
