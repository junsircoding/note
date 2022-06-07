#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : Scripts/1-获取当前文件目录.py
# @Info        : 
# @Last Edited : 2022-06-07 11:16:41

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
