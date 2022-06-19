#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 01-Scripts/01-获取当前文件目录.py
# @Info        : 
# @Last Edited : 2022-06-19 21:07:34

import os
import sys
"""
当前目录，相当于 `pwd`
"""
pwd = os.path.dirname(os.path.abspath(__file__))
"""
分拆
"""
path_list = pwd.split(os.sep)
"""
取上级目录，相当于 `cd ..`
"""
path = os.sep.join(path_list[:-1])
"""
将某个目录加入环境变量
"""
sys.path.insert(0, os.path.join(path))


import os

# 获取当前目录
print(os.getcwd())
print(os.path.abspath(os.path.dirname(__file__)))

# 获取上级目录
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))

# 获取上上级目录
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))
