#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : 01-Scripts/03-Web框架中读取上下文.py
# @Info        : 
# @Last Edited : 2022-06-07 17:46:48

import os
import sys


# 当前文件绝对路径
pwd = os.path.dirname(os.path.abspath(__file__))
# 分拆
path_list = pwd.split(os.sep)
# 取当前目录, 即在路径中去掉当前文件名称
path = os.sep.join(path_list[:-1])
# 将当前目录加入环境变量
sys.path.insert(0, os.path.join(path))

for path in sys.path:
    print(path)
