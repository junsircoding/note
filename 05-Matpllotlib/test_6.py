#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 05-Matpllotlib/test_6.py
# @Info        : 
# @Last Edited : 2022-06-08 18:04:57

"""柱状图"""
import matplotlib.pyplot as plt
# 0.准备数据
# 电影名字
movie_name = ['雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记',
              '全球风暴', '降魔传', '追捕', '七十七天', '密战', '狂兽', '其它']
# 横坐标
x = range(len(movie_name))
# 票房数据
y = [73853, 57767, 22354, 15969, 14839, 8725, 8716, 8318, 7916, 6764, 52222]

# 1.创建画布
plt.figure(figsize=(20, 8), dpi=100)

# 2.绘制柱状图
plt.bar(x, y, width=0.5, color=['b', 'r', 'g',
        'y', 'c', 'm', 'y', 'k', 'c', 'g', 'b'])

# 2.1b修改x轴的刻度显示
plt.xticks(x, movie_name)

# 2.2 添加网格显示
plt.grid(linestyle="--", alpha=0.5)

# 2.3 添加标题
plt.title("电影票房收入对比")

# 3.显示图像
plt.show()
