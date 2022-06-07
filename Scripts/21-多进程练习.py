#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : Scripts/21-多进程练习.py
# @Info        : 
# @Last Edited : 2022-06-07 11:19:15

import multiprocessing
from multiprocessing import Manager


def worker(procnum, return_list):
    '''worker function'''
    print(str(procnum) + ' represent!')
    return_list.append(procnum)


if __name__ == '__main__':
    manager = Manager()
    return_list = manager.list() # 也可以使用列表list
    # return_dict = manager.dict()
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i, return_list))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print(return_list)
