#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : 01-Scripts/07-读取yaml配置文件.py
# @Info        : 
# @Last Edited : 2022-06-07 14:37:18

"""
读取 yaml 配置文件
pip install pyyaml
"""

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

with open("config.yaml" , "r", encoding="utf-8") as f:
    config = load(f, Loader=Loader)
