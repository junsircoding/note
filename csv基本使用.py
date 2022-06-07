#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : csv基本使用.py
# @Info        : 
# @Last Edited : 2022-06-07 10:59:16

"""
csv 基本使用
"""

import csv
import chardet

# 检测文件编码
with open("./data.csv", "rb") as f:
    data = f.read()
    chardet.detect(data)

# 读取 csv 文件
with open("./data.csv", "r", encoding="utf-8") as f:
    csv_reader = csv.reader(f, delimiter=",")
    data_list = [row for row in csv_reader]

# 新建 csv 文件
data_list = [
    ["春", "眠", "不", "觉", "晓"],
    ["处", "处", "闻", "啼", "鸟"],
    ["夜", "来", "风", "雨", "声"],
    ["花", "落", "知", "多", "少"]
]
with open("./data2.csv", "w", encoding="utf-8-sig", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["第一列", "第二列", "第三列", "第四列", "第五列"])
    csv_writer.writerows(data_list)
