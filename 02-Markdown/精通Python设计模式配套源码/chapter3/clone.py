#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 02-Markdown/精通Python设计模式配套源码/chapter3/clone.py
# @Info        : 
# @Last Edited : 2022-06-14 22:22:27

import copy


class A:

    def __init__(self):
        self.x = 18
        self.msg = 'Hello'


class B(A):

    def __init__(self):
        A.__init__(self)
        self.y = 34

    def __str__(self):
        return '{}, {}, {}'.format(self.x, self.msg, self.y)

if __name__ == '__main__':
    b = B()
    c = copy.deepcopy(b)
    print([str(i) for i in (b, c)])
    print([i for i in (b, c)])
