#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : 短笔记/精通Python设计模式配套源码/chapter1/id.py
# @Info        : 
# @Last Edited : 2022-06-07 10:59:16

class A(object):
    pass

if __name__ == '__main__':
    a = A()
    b = A()

    print(id(a) == id(b))
    print(a, b)
