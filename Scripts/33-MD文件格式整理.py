#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : Scripts/33-MD文件格式整理.py
# @Info        : 
# @Last Edited : 2022-06-07 11:19:15

"""
将格式混乱的 md 文件整理, 英文数字前后空一格
"""
import re

old_file = "/Users/junsircoding/Downloads/网盘文件/00-系统/有关UEFI资料的收集.md"
new_file = f"{old_file[:-3]}_new.md"

# 读取文件
with open(old_file, "r", encoding="utf-8") as f:
    data = f.read()
# 将字符拆开放到列表
str_list = []
for char in data:
    str_list.append(char)
"""
正则识别
字符前是中文,后是英文,该字符前面插入空格
字符前是英文,后是中文,该字符后面插入空格
"""
new_str_list = []
for idx, item in enumerate(str_list):
    if idx in (0, len(str_list)-1):
        new_str_list.append(item)
        continue
    elif idx not in (0, len(str_list)-1):
        last = str_list[idx-1]
        next = str_list[idx+1]
        if item != " " and bool(re.search('[a-zA-Z]', item)):
            if (not bool(re.search('[a-zA-Z]', last))) and bool(re.search('[a-zA-Z]', next)) and (not bool(re.search('[0-9]', last))):
                new_str_list.append(" ")
                new_str_list.append(item)
            elif (not bool(re.search('[a-zA-Z]', next))) and bool(re.search('[a-zA-Z]', last)) and (not bool(re.search('[0-9]', next))):
                new_str_list.append(item)
                new_str_list.append(" ")
            else:
                new_str_list.append(item)
        elif item != " " and bool(re.search('[0-9]', item)):
            if (not bool(re.search('[0-9]', last))) and bool(re.search('[0-9]', next)) and (not bool(re.search('[a-zA-Z]', last))):
                new_str_list.append(" ")
                new_str_list.append(item)
            elif (not bool(re.search('[0-9]', next))) and bool(re.search('[0-9]', last)) and (not bool(re.search('[a-zA-Z]', next))):
                new_str_list.append(item)
                new_str_list.append(" ")
            else:
                new_str_list.append(item)
        elif item == "。":
            new_str_list.append("\n")
        elif item == " ":
            if ("\u4e00" <= last <= "\u9fff" and "\u4e00" <= next <= "\u9fff") or\
                (bool(re.search('[a-zA-Z]', last)) and bool(re.search('[a-zA-Z]', next))):
                continue
        elif item == "\n":
            if last != "。":
                continue
            else:
                new_str_list.append(item)
        else:
            new_str_list.append(item)

# 输出新文件
with open(new_file, "w", encoding="utf-8") as f2:
    f2.write("".join(new_str_list))
