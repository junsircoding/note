#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 01-Scripts/09-系统监控和网络监控.py
# @Info        : 
# @Last Edited : 2022-06-08 18:04:57

"""
系统监控和网络监控
"""

import psutil
import time
import datetime
from threading import Timer


def MonitorSystem(logfile=None):
    cpuper = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    memper = mem.percent
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} cpu:{cpuper}%, mem:{memper}%'
    print('current sys status:', line)
    if logfile:
        logfile.write(line)
    Timer(3, MonitorSystem).start()


def loopMonitor():
    for i in range(10):
        MonitorSystem()
        time.sleep(3)


def MonitorNetWork(logfile=None):
    netinfo = psutil.net_io_counters()
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} bytessent={netinfo.bytes_sent}, bytesrecv={netinfo.bytes_recv}'
    print('current net status:', line)
    if logfile:
        logfile.write(line)
    Timer(1, MonitorNetWork).start()

# print(datetime.datetime.now())
# sTimer = Timer(3, MonitorSystem)
# nTimer = Timer(1, MonitorNetWork)
# sTimer.start()
# nTimer.start()

# sTimer.join()
# nTimer.join()
# print(datetime.datetime.now())


MonitorSystem()
MonitorNetWork()
