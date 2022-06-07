import os
import re
import time


# 获取根目录
# 当前文件绝对路径
pwd = os.path.dirname(os.path.abspath(__file__))
# 分拆
path_list = pwd.split(os.sep)
# 取当前目录, 即在路径中去掉当前文件名称
path = os.sep.join(path_list[:-1])

# 遍历根目录下所有 py 文件
py_file_list = []
for root, dirs, files in os.walk(path):
    for file_name in files:
        if file_name.endswith(".py"):
            py_file_list.append(os.sep.join([root, file_name]))

# 检查文件前 7 行内容
# 如果不是模块注释, 插入该内容
# 如果是, 除创建日期之外全部覆盖
for file_abs_path in py_file_list:
    line_5 = "# @Info        : "
    line_2 = f"# @Date        : {time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())}"
    print(f"处理文件: {file_abs_path}")

    with open(file_abs_path, "r", encoding="utf-8") as f:
        rest_text = ""
        is_docstring = True
        # 记录旧的 docstring
        for line_idx, line in enumerate(f.readlines()):
            line_strip = line.strip()

            if line_idx == 0:
                if not re.compile(r"^#!/usr/bin/env python.*$").search(line_strip):
                    is_docstring = False
                line_0 = line_strip
            elif line_idx == 1:
                if not re.compile(r"^# \-\*\-.*$").search(line_strip):
                    is_docstring = False
                line_1 = line_strip
            elif line_idx == 2:
                if not re.compile(r"^# @Date.*$").search(line_strip):
                    is_docstring = False
                line_2 = line_strip
            elif line_idx == 3:
                if not re.compile(r"^# @Author.*$").search(line_strip):
                    is_docstring = False
                line_3 = line_strip
            elif line_idx == 4:
                if not re.compile(r"^# @File.*$").search(line_strip):
                    is_docstring = False
                line_4 = line_strip
            elif line_idx == 5:
                if not re.compile(r"^# @Info.*$").search(line_strip):
                    is_docstring = False
                line_5 = line_strip
            elif line_idx == 6:
                if not re.compile(r"^# @Last.*$").search(line_strip):
                    is_docstring = False
                line_6 = line_strip
            else:
                rest_text = rest_text + line
        
        if not is_docstring:
            rest_text = ""
            for _line in f.readlines():
                if _line.strip().startswith("#"):
                    pass
                else:
                    rest_text = rest_text + _line

        rel_file_name = os.sep.join(re.findall(r"(?<=note/).*$", file_abs_path)[0].split("/"))
        # 赋值新的 dicstring 行
        line_0 = "#!/usr/bin/env python"
        line_1 = "# -*- coding: utf-8 -*-"
        line_3 = "# @Author      : junsircoding"
        line_4 = f"# @File        : {rel_file_name}"
        line_6 = f"# @Last Edited : {time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())}"

        # 组成新的全文
        new_text = "\n".join([line_0,line_1,line_2,line_3,line_4,line_5,line_6]) + "\n"
        new_text = new_text + rest_text

    with open(file_abs_path, "w", encoding="utf-8") as f:
        f.write(new_text)

    
