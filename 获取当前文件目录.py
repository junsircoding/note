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