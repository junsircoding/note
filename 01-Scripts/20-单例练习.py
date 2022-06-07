#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : 01-Scripts/20-单例练习.py
# @Info        : 
# @Last Edited : 2022-06-07 14:37:18

"""
单例模式的数据存储
当需要缓存的数据实时加载需要一定的时间, 但是不会频繁地更新, 就可以用这种方法. 
"""

import time
import traceback
# 导入自定义日志
logger = object


class Updater(object):
    """定时刷新器
    用于间隔一段时间从 DB 或本地数据中取出数据
    避免对 DB 造成太大压力, 用于更新不频繁的数据读取
    """
    DEFAULT_UPDATE_INTERVAL = 300  # 默认 300 秒

    def __init__(self, interval=DEFAULT_UPDATE_INTERVAL):
        """初始化

        Args:
            interval(int): 默认数据刷新时间间隔
        """
        # 数据刷新时间间隔
        self.interval = interval
        # 最近一次的刷新时间
        self.last_update_time = 0
        # 刷新标志
        self.is_updated = True
        # 提示信息
        self.info = ""
        if self.check_update():
            self.do_update()

    def __set_info(self, info):
        """提示日志

        Args:
            info(str): 日志文本
        """
        logger.info("提示信息[%s]" % info)

    def __set_error(self, str_error):
        """错误日志

        Args:
            str_error(str): 报错日志文本
        """
        self.info = str_error
        logger.error("错误信息 [%s]" % str_error)

    def load(self):
        """加载数据核心类, 需要在子类中继承
        """
        raise Exception("这个方法必须在子类中重写")

    def close(self):
        """关闭刷新
        """
        self.is_updated = False

    def open(self):
        """开启刷新
        """
        self.is_updated = True

    def do_update(self):
        """执行刷新动作

        Returns:
            (bool): 刷新布尔标志
        """
        load_ret = False
        try:
            self.load()
            load_ret = True
        except Exception as ex:
            self.__set_error(traceback.format_exc())
            load_ret = False
        finally:
            self.last_update_time = time.time()
        return load_ret

    def check_update(self):
        """检查数据是否已经刷新

        Returns:
            (bool): 刷新布尔标志
        """
        if self.is_updated is False:
            self.__set_info("update 函数已经关闭, 无法更新数据")
            return False
        if time.time() - self.last_update_time <= self.interval:
            return False
        return True

    @staticmethod
    def update(func):
        """刷新动作

        Returns:
            (func): 被装饰的函数
        """
        def warp(*args, **kwargs):
            self = args[0]
            # 检查是否需要刷新
            if self.check_update() is True and self.do_update() is False:
                raise Exception(
                    "[%s]更新数据发生异常: %s" % (func.func_name, self.info)
                )
            return func(*args, **kwargs)
        return warp

    def reset(self):
        """重置内容
        """
        self.last_update_time = 0


class DemoCache(Updater, list):
    """测试用例
    """

    def __init__(self, interval):
        Updater.__init__(self, interval=interval)

    def __new__(cls, *args, **kwargs):
        """单例模式
        """
        if not hasattr(cls, "_instance"):
            obj_instance = super(DemoCache, cls)
            cls._instance = obj_instance.__new__(cls, *args, **kwargs)
        return cls._instance

    def load(self):
        """加载数据
        """
        self.append(str(time.time()))

    @Updater.update
    def get(self):
        """取数据
        
        Returns:
            数据
        """
        if len(self) == 0:
            return None
        else:
            return self[-1]


"""
# Updater 测试用例
demo = DemoCache(interval=10)
while True:
    print("*" * 50)
    print("demo get: %s" % demo.get())
    print("demo is: {}".format(demo))
    time.sleep(2)
"""


class DataCache(Updater, dict):
    """数据容器
    """

    def __init__(self, interval):
        Updater.__init__(self, interval=interval)

    def __new__(cls, *args, **kwargs):
        """单例模式
        """
        if not hasattr(cls, "_instance"):
            obj_instance = super(DataCache, cls)
            cls._instance = obj_instance.__new__(cls, *args, **kwargs)
        return cls._instance

    def load(self):
        """加载数据
        """
        self["data"] = load_data()

    @Updater.update
    def get(self):
        """取数据
        
        Returns:
            数据
        """
        if len(self) == 0:
            return None
        else:
            return self["data"]


def load_data():
    """加载数据
    """


# 实例化缓存
data_cache = DataCache(interval=60*60*24)

"""
# 单例缓存测试用例
data = data_cache.get()
if data is None:
    data = load_data()
"""
