#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:27:31
# @Author      : junsircoding@gmail.com
# @File        : 01-Scripts/00-生成模块开头注释.py
# @Info        : 
# @Last Edited : 2022-06-14 22:22:27

import os
import re
import time

# 获取所有 py 文件路径
pwd = os.path.dirname(os.path.abspath(__file__))
path_list = pwd.split(os.sep)
path = os.sep.join(path_list[:-1])

py_file_list = []
for root, dirs, files in os.walk(path):
    for file_name in files:
        if file_name.endswith(".py"):
            py_file_list.append(os.sep.join([root, file_name]))

# 注释文本的正则模式
pattern_list = [
    re.compile(r"^#!/usr/bin/env python.*$"),
    re.compile(r"^# \-\*\-.*$"),
    re.compile(r"^# @Date.*$"),
    re.compile(r"^# @Author.*$"),
    re.compile(r"^# @File.*$"),
    re.compile(r"^# @Info.*$"),
    re.compile(r"^# coding: utf-8$"),
    re.compile(r"^# @Last.*$")
]

current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

# 记录每个文件内容, 去除前七行的注释内容
for file_abs_path in py_file_list:
    create_time = current_time
    file_info = ""
    print(f"处理文件: {file_abs_path}")
    # 跳过当前文件
    # if file_abs_path == os.path.abspath(__file__):
    #     continue
    with open(file_abs_path, "r", encoding="utf-8") as f:
        rest_text = ""
        for _idx, _line in enumerate(f.readlines()):
            is_docstring = False
            # 如果有注释, 不记录
            for p_idx, pattern in enumerate(pattern_list):
                if pattern.search(_line.strip()):
                    # 记录创建时间
                    if p_idx == 2:
                        create_time = _line.replace("# @Date        : ", "").strip()
                    # 记录文件描述
                    if p_idx == 5:
                        file_info = _line.replace("# @Info        :", "").strip()
                    is_docstring = True
            if is_docstring:
                continue
            rest_text = rest_text + _line
        # 注释与代码之间有一个空行, 文件末尾有一个空行
        rest_text = rest_text.strip()
        rest_text = "\n" + "\n" + rest_text + "\n"

    # 将新的注释和文件内容合并, 覆盖原文件内容
    rel_file_name = os.sep.join(re.findall(r"(?<=note/).*$", file_abs_path)[0].split("/"))
    line_0 = "#!/usr/bin/env python"
    line_1 = "# -*- coding: utf-8 -*-"
    line_2 = f"# @Date        : {create_time}"
    line_3 = "# @Author      : junsircoding@gmail.com"
    line_4 = f"# @File        : {rel_file_name}"
    line_5 = "# @Info        : "
    line_6 = f"# @Last Edited : {current_time}"

    new_text = "\n".join([line_0, line_1, line_2, line_3, line_4, line_5, line_6])
    new_text = new_text + rest_text

    with open(file_abs_path, "w", encoding="utf-8") as f:
        f.write(new_text)
