#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : 01-Scripts/06-读取json配置文件.py
# @Info        : 
# @Last Edited : 2022-06-07 14:37:18

"""
读取 json 配置文件
"""
import json


with open("./config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
