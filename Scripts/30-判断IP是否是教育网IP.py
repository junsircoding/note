#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : Scripts/30-判断IP是否是教育网IP.py
# @Info        : 
# @Last Edited : 2022-06-07 11:19:15

"""
判断 IP 是否是 教育网 IP
"""

import IPy

import re
import requests


def is_edu_id(ip):
    # 1. 从 http://ipcn.chacuo.net/view/i_CERNET 获取教育网ip列表
    response = requests.get("http://ipcn.chacuo.net/down/t_txt=c_CERNET")
    te = response.text
    te = te.split('\r\n')
    te_new = []
    for i in range(1, len(te)-1):
        te_new.append(te[i])
    # 第一主机位列表
    ip_l = []
    for i in te_new:
        ip_l.append(i.split('\t')[0])
    # 最后主机位列表
    mask_l = []
    for i in te_new:
        mask_l.append(i.split('\t')[1])
    
    # 2. 判断 ip 是否是 教育网 ip
    flag = False
    for i in range(len(ip_l)):
        if ip in IPy.IP(ip_l[i] + '-' + mask_l[i]):
            flag = True
            break
        else:
            flag = False

    return flag
