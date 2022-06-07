#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : 01-Scripts/12-判断数字是否为奇数.py
# @Info        : 
# @Last Edited : 2022-06-07 14:37:18

"""
◇filter(func, iter)

    参数含义同 map
    filter() 会把 iter 的每个元素传给 func，如果 func 返回结果为 True，就把元素保存在一个 list 中，最后返回此 list。
    举例:
    要过滤出所有奇数，代码如下:

filter(odd, [1, 2, 3])  # 返回[1, 3]


Python 中的 filter 函数非常有用。使用 filter 函数可以从一个数据集里面筛选出我们想要的数据，而这个筛选规则可以自定义。
filter 函数有两个参数，第一个是自定义的筛选规则函数，第二个是数据集。
比如我们要筛选出一个列表中的偶数，可以先定义一个判断数字是否为奇数的函数


一个数据集为

那么 filter 可以这样使用
filter(is_odd, dada)

此处可以用上 lambda，把代码简化为一行:
filter(lambda n: (n%2)==1, lst)

"""


def is_odd(num: int) -> bool:
    """
    判断数字是否为奇数
    """
    return (num % 2) == 1


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = filter(is_odd, data)
