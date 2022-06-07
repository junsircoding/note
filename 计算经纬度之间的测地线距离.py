#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : 计算经纬度之间的测地线距离.py
# @Info        : 
# @Last Edited : 2022-06-07 10:59:16

"""
计算经纬度之间的测地线距离
纬度 latitude, 经度 longitude
纬度 ±0.01, 测地线距离 ±1.105746174097012 KM
经度 ±0.01, 测地线距离 ±1.1130264976969 KM
pip install geopy
"""

from geopy.distance import geodesic

geodesic((40, 160), (40.1, 160.1)).km # 参数顺序: 纬度, 经度
