#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 02-Markdown/精通Python设计模式配套源码/chapter5/mymath.py
# @Info        : 
# @Last Edited : 2022-06-19 21:07:34

import functools


def memoize(fn):
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer


@memoize
def nsum(n):
    '''返回前n个数字的和'''
    assert(n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n-1)


@memoize
def fibonacci(n):
    '''返回斐波那契数列的第n个数'''
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    from timeit import Timer
    measure = [{'exec': 'fibonacci(100)', 'import': 'fibonacci',
                'func': fibonacci}, {'exec': 'nsum(200)', 'import': 'nsum',
                                     'func': nsum}]
    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import \
            {}'.format(m['import']))
        print('name: {}, doc: {}, executing: {}, time: \
            {}'.format(m['func'].__name__, m['func'].__doc__,
                       m['exec'], t.timeit()))
