#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : 01-Scripts/29-爬虫封装调度方法.py
# @Info        : 
# @Last Edited : 2022-06-07 14:37:18

"""
爬虫封装调度方法
"""

import requests
import json
import time


class XXX(object):
    # 初始化
    def __init__(self):
        self.url = 'https://baike.baidu.com/wikitag/api/getlemmas'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }

    # 发送请求
    def send_request(self, form_data):
        response = requests.post(
            url=self.url, headers=self.headers, data=form_data).text
        return response

    # 解析数据
    def jiexi_data(self, data):
        dict_data = json.loads(data)
        return dict_data

    # 写入文件
    def write_file(self):
        pass

    # 调度方法
    def run(self):
        for page in range(0, 999):
            form_data = {
                'limit': '24',
                'timeout': '3000',
                'filterTags': '[]',
                'tagId': '75953',
                'fromLemma': 'false',
                'contentLength': '40',
                'page': page
            }
            json_data = self.send_request(form_data)
            dict_data = self.jiexi_data(json_data)
            for name in dict_data['lemmaList']:
                print(name['lemmaId'], name['lemmaTitle'],
                      name['lemmaDesc'], name['lemmaUrl'])


if __name__ == '__main__':
    x = XXX()
    x.run()
