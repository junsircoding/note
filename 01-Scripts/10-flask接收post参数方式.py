#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : 01-Scripts/10-flask接收post参数方式.py
# @Info        : 
# @Last Edited : 2022-06-07 16:57:45

from flask import Flask
from flask import request
from flask import jsonify


application = Flask(__name__)

@application.route("/login", methods=["GET", "POST"])
def login():
    """获取 application/json post 数据"""
    if request.method == "POST":
        return jsonify(request.json)

@application.route("/login1", methods=["GET", "POST"])
def login_1():
    """获取 form data 数据"""
    if request.method == "POST":
        return jsonify(request.form)

@application.route("/login2", methods=["GET", "POST"])
def login_2():
    """获取 form data 数据"""
    if request.method == "POST":
        return jsonify(request.form)

@application.route("/login3", methods=["GET", "POST"])
def login_3():
    """获取 text/plain 数据"""
    if request.method == "POST":
        import json
        origin_data = request.data
        print(f"origin_data: {origin_data}")
        data_decode = origin_data.decode()
        print(f"data_decode: {data_decode}")
        data_to_json = json.loads(data_decode)
        print(f"data_to_json: {data_to_json}")
        return jsonify(data_to_json)



if __name__ == "__main__":
    application.run(host="0.0.0.0", port=30381, debug=True)
