#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-09 14:57:29
# @Author      : junsircoding@gmail.com
# @File        : 01-Scripts/14-爬取租房信息.py
# @Info        : 
# @Last Edited : 2022-06-19 21:07:34

import json
import requests

url = "https://jinshuju.net/f/I18O8b/s/GtbEE0?q%5B0%5D%5Bfield_5%5D=&q%5B1%5D%5Bfield_4%5D=n5d1&embedded="

resp = requests.get(url).text
with open("./data.html", "w", encoding="utf-8") as f:
    f.write(resp)
"""
tbody 之间的数据
所有的 tr
每个 tr 有 7 个 td
"""
