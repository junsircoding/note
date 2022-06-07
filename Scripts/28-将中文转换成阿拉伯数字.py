#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : Scripts/28-将中文转换成阿拉伯数字.py
# @Info        : 
# @Last Edited : 2022-06-07 11:16:41

"""
将中文转换成阿拉伯数字,整数部分 如七百二十四-> 724
"""

import re


def to_num(cnnumber):
    UTIL_CN_NUM = {
        '零': 0, '一': 1, '二': 2, '三': 3, '四': 4,
        '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
        '两': 2,
        '壹': 1, '贰': 2, '叁': 3, '肆': 4, '伍': 5,
        '陆': 6, '柒': 7, '捌': 8, '玖': 9, '拾': 10,
        '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000,
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    }

    numberlist = []
    totallist = []

    flag = re.search('亿', cnnumber)

    if flag:
        numberlist = re.split('亿', cnnumber)
    else:
        numberlist.append(cnnumber)

    for numberstr in numberlist:
        unit = 1  # 表示单位：个十百千...
        total = 0
        for i in range(len(numberstr) - 1, -1, -1):
            val = UTIL_CN_NUM[numberstr[i]]
            if val == 10 and i == 0:  # 应对 十三 十四 十*之类
                unit = val
                total = total + val
            if val >= 10:
                if unit >= 10000:
                    unit = 10000 * val
                else:
                    unit = val
            else:
                total = total + unit * val
        totallist.append(total)
    if len(totallist) > 1:
        total = totallist[0] * UTIL_CN_NUM['亿'] + totallist[1]
    else:
        total = int(totallist[0])

    return total

print(to_num("十八"))
