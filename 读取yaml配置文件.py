"""
读取 yaml 配置文件
pip install pyyaml
"""

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

with open("config.yaml" , "r", encoding="utf-8") as f:
    config = load(f, Loader=Loader)