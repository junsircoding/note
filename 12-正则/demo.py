#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : 12-正则/demo.py
# @Info        : 
# @Last Edited : 2022-06-07 17:46:48

"""
Python 正则测试用例
"""

import re


pattern = re.compile(ur'^[0-9]*$')
str = u'12345'
print(pattern.search(str))
