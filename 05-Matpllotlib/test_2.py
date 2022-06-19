#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 05-Matpllotlib/test_2.py
# @Info        : 
# @Last Edited : 2022-06-19 21:07:34

"""matplotlib 画出温度变化图"""
import matplotlib.pyplot as plt
import random


x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
# 增加北京的温度数据
y_beijing = [random.uniform(1, 3) for i in x]
# 创建画布
plt.figure(figsize=(20, 8), dpi=80)
# 绘制折线图
plt.plot(x, y_shanghai, label="Shanghai")
# 使用多次plot可以画多个折线
plt.plot(x, y_beijing, color='r', linestyle='--', label="Beijing")
# 构造x轴刻度标签
x_sticks_label = [f"11:{i}" for i in x]
# 构造y轴刻度
y_sticks = range(40)
# 修改 x, y 轴坐标的刻度显示
plt.xticks(x[::5], x_sticks_label[::5])
plt.yticks(y_sticks[::5])
# 添加网格显示
plt.grid(True, linestyle='--', alpha=0.5)
# 横轴名称
plt.xlabel("Time")
# 纵轴名称
plt.ylabel("Tempreture")
# 标题
plt.title("11:00:00 AM TO 12:00:00 Tempreture Change Figure", fontsize=20)
# 保存图片到指定路径
plt.savefig("test.png")
# 显示图例
plt.legend(loc="best")
# 显示图像
plt.show()
