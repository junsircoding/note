#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : Scripts/26-机器人对话新冠确诊分析数据梳理.py
# @Info        : 
# @Last Edited : 2022-06-07 11:19:15

"""
机器人对话新冠确诊分析数据梳理
"""

import re
import json
import requests

from bs4 import BeautifulSoup
from openpyxl import Workbook
from prettytable import ALL
from prettytable import PrettyTable

f = 0


class CityCode(object):
    hubei = {}
    guangdong = {}
    zhejiang = {}
    beijing = {}
    shanghai = {}
    hunan = {}
    anhui = {}
    chongqing = {}
    sichuan = {}
    shandong = {}
    guangxi = {}
    fujian = {}
    jiangsu = {}
    henan = {}
    hainan = {}
    tianjin = {}
    jiangxi = {}
    shannxi = {}  # 陕西
    guizhou = {}
    liaoning = {}
    xianggang = {}
    heilongjiang = {}
    aomen = {}
    xinjiang = {}
    gansu = {}
    yunnan = {}
    taiwan = {}
    shanxi2 = {}  # 山西
    jilin = {}
    hebei = {}
    ningxia = {}
    neimenggu = {}
    qinghai = {}  # none
    xizang = {}  # none
    provinces_idx = [hubei, guangdong, zhejiang, chongqing, hunan, anhui, beijing,
                     shanghai, henan, guangxi, shandong, jiangxi, jiangsu, sichuan,
                     liaoning, fujian, heilongjiang, hainan, tianjin, hebei, shanxi2,
                     yunnan, xianggang, shannxi, guizhou, jilin, gansu, taiwan,
                     xinjiang, ningxia, aomen, neimenggu, qinghai, xizang]
    map = {
        '湖北': 0, '广东': 1, '浙江': 2, '北京': 3, '上海': 4, '湖南': 5, '安徽': 6, '重庆': 7,
        '四川': 8, '山东': 9, '广西': 10, '福建': 11, '江苏': 12, '河南': 13, '海南': 14,
        '天津': 15, '江西': 16, '陕西': 17, '贵州': 18, '辽宁': 19, '香港': 20, '黑龙江': 21,
        '澳门': 22, '新疆': 23, '甘肃': 24, '云南': 25, '台湾': 26, '山西': 27, '吉林': 28,
        '河北': 29, '宁夏': 30, '内蒙古': 31, '青海': 32, '西藏': 33
    }

    def __init__(self):
        """
        初始化 Excel 对象
        """
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append([])
        self.ws.append([
            '一级分类/二级分类/三级分类/四级分类/五级分类',
            '标准问题', '通用渠道答案', 'WEB答案', 'WAP答案',
            'APP答案', '微信公众号答案', '微信小程序答案', '电话答案',
            '相似问题1', '相似问题2', '相似问题3', '相似问题4', '相似问题5', '相似问题6'
        ])

    def save_excel(self, item):
        """
        保存数据
        """
        global f

        self.ws.append(item)
        self.wb.save(r'result.xlsx')
        f += 1
        print('数据梳理写入成功------------------', f)
        print(item, '数据梳理写入成功---{}'.format(f))

    def is_json(self, json_str):
        """
        判断是否为 Json 数据
        """
        try:
            json.loads(json_str)
        except ValueError:
            return False
        return True

    def main(self):
        url = "https://3g.dxy.cn/newh5/view/pneumonia"

        try:
            headers = {}
            headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
                                    'AppleWebKit/537.36 (KHTML, like Gecko) '\
                                    'Chrome/70.0.3538.77 Safari/537.36'  # http 头大小写不敏感
            headers['accept'] = 'text/html,application/xhtml+xml,'\
                                'application/xml;q=0.9,image/webp,'\
                                'image/apng,*/*;q=0.8'
            headers['Connection'] = 'keep-alive'
            headers['Upgrade-Insecure-Requests'] = '1'

            r = requests.get(url, headers=headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'html.parser')
            table = PrettyTable(['地区', '确诊', '死亡', '治愈'])
            table.hrules = ALL

            json_provinces = re.findall("{\"provinceName\":(.*?)]}", str(soup))

            idx = 0
            new_list = []
            for province in json_provinces:
                if self.is_json(province):
                    pass
                else:
                    province = "{\"provinceName\":" + province + "]}"
                    province = json.loads(province)

                province_name = province['provinceShortName'] if province['provinceShortName'] != 0 else '-'
                confirmed = province['confirmedCount'] if province['confirmedCount'] != 0 else '-'
                suspected = province['suspectedCount'] if province['suspectedCount'] != 0 else '-'
                cured = province['curedCount'] if province['curedCount'] != 0 else '-'
                dead = province['deadCount'] if province['deadCount'] != 0 else '-'
                new_list.append([province_name, confirmed, dead, cured])
                self.map[province_name] = idx
                idx = idx + 1
                for city in province['cities']:
                    self.provinces_idx[self.map[province_name]][city['cityName']] = [city['confirmedCount'],
                                                                                     city['deadCount'],
                                                                                     city['curedCount']]
            data_list = [0 if d == '-' else d for i in new_list for d in i]
            all_products = [data_list[i:i + 4]
                            for i in range(0, len(data_list), 4)]
            # print(all_products)
            # return all_products,
            j_list = []
            for i in all_products:
                j_list.append(['防疫知识', str(i[0]) + '确诊病例是多少',
                               str(i[0]) + '疫情数据变化如下：' + '累计确诊' + str(i[1]) + '例' + ',' + '死亡' + str(
                                   i[2]) + '例' + ',' + '治愈' + str(i[3]) + '例' + ',', '', '', '', '', '',
                               '',
                               '<*>' + str(i[0]) + ' ' + '{确诊,疑似,死亡,治愈,今日确诊,今日疑似,今日死亡,今日治愈}' + ' ' + '{病例,疫情}', ])
            return j_list
        except Exception as ex:
            print(f"连接失败:{str(ex)}")

    def parse(self):
        url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
        resp = requests.get(url=url)
        epidemic = json.loads(resp.text)
        data = json.loads(epidemic['data'])
        data_list = []
        china_total = data['chinaTotal']
        china = ['中国确诊病例是多少']
        data_str_list = ['防疫知识']
        new_data_list = data_list + data_str_list + china

        for key in china_total:
            new_data_list.append(china_total[key])
        # print(new_data_list, '----7878')
        new1_data_list = [new_data_list[0], new_data_list[1],
                          '中国疫情数据变化如下：' + '累计确诊' + str(new_data_list[2]) + '例' + ',' + '疑似' + str(new_data_list[
                              3]) + '例' + ',' + '死亡' + str(
                              new_data_list[4]) + '例' + ',' + '治愈' + str(new_data_list[
                                  5]) + '例' + ',', '', '', '', '', '',
                          '',
                          '<*>' + '中国' + ' ' + '{确诊,疑似,死亡,治愈,今日确诊,今日疑似,今日死亡,今日治愈}' + ' ' + '{病例,疫情}', ]
        total_list = []
        total_list.append(new1_data_list)
        new_data = data['areaTree']

        for data_tex in new_data:
            if data_tex['name'] == '中国':
                china_list_data = data_tex['children']
                for china_data in china_list_data:
                    name = china_data['name']
                    # print(name,'------------------666')
                    name_data = china_data['children']
                    flag = []
                    for new_str in name_data:
                        result1_name = '防疫知识'
                        new_name = name + new_str['name'] + '确诊病例是多少'
                        area_list = [new_str['total'][data_str]
                                     for data_str in new_str['total']]
                        today_list = [new_str['today'][data_today]
                                      for data_today in new_str['today']]
                        new_data_str = area_list + today_list
                        # print(new_data_str,'--------000')
                        flag.append(new_data_str)
                        answer = [
                            name + new_str['name'] + '疫情数据变化如下：' + '累计确诊' + str(
                                new_data_str[0]) + '例' + ',' + '疑似' + str(
                                new_data_str[
                                    1]) + '例' + ',' + '死亡' + str(new_data_str[2]) + '例' + ',' + '治愈' + str(new_data_str[
                                        3]) + '例' + ',' + '今日确诊' + str(
                                new_data_str[4]) + '例' + ',' + '今日疑似' + str(new_data_str[
                                    5]) + '例' + '，' + '今日死亡' + str(
                                new_data_str[6]) + '例' + '，' + '今日治愈' + str(new_data_str[
                                    7]) + '例' + ',', '', '', '', '', '', '',
                            '<*>' +
                            new_str['name'] + ' ' +
                            '{确诊,疑似,死亡,治愈,今日确诊,今日疑似,今日死亡,今日治愈}' + ' ' + '{病例,疫情}',
                        ]

                        answer.insert(0, result1_name)
                        answer.insert(1, new_name)
                        answer.insert(2, new_data_list[1])
                        total_list.append(answer)
            else:
                result_name = '防疫知识'
                foreign_name = data_tex['name'] + '确诊病例是多少'
                foreign_area_list = [new_str['total'][data_str]
                                     for data_str in data_tex['total']]
                foreign_today_list = [new_str['today'][data_today]
                                      for data_today in data_tex['today']]
                new_foreign_list = foreign_area_list + foreign_today_list

                answer_tex = [
                    data_tex['name'] + '疫情数据变化如下：' + '累计确诊' + str(new_foreign_list[0]) + '例' + ',' + '疑似' + str(
                        new_foreign_list[
                            1]) + '例' + ',' + '死亡' + str(new_foreign_list[2]) + '例' + ',' + '治愈' + str(new_foreign_list[
                                3]) + '例' + ',' + '今日确诊' + str(
                        new_foreign_list[4]) + '例' + ',' + '今日疑似' + str(new_foreign_list[
                            5]) + '例' + '，' + '今日死亡' + str(
                        new_foreign_list[6]) + '例' + '，' + '今日治愈' + str(new_foreign_list[
                            7]) + '例' + ',' + ',', '', '', '', '', '',
                    '',
                    '<*>' + data_tex['name'] + ' ' + '{确诊,疑似,死亡,治愈,今日确诊,今日疑似,今日死亡,今日治愈}' + ' ' + '{病例,疫情}', ]
                answer_tex.insert(0, result_name)
                answer_tex.insert(1, new_data_list[1])
                answer_tex.insert(2, foreign_name)
                total_list.append(answer_tex)

        new_data_tex = [total_list[0]]
        list_ch = []
        for a in total_list[1:]:
            a.remove('中国确诊病例是多少')
            list_ch.append(a)
        new_total_list = new_data_tex + list_ch
        new_province = self.main()
        new_list_data = new_total_list

        for k in new_list_data:
            self.save_excel(k)


if __name__ == '__main__':
    sit_tex = CityCode()
    sit_tex.parse()
    sit_tex.main()
