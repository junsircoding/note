#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 05-Matpllotlib/test_3.py
# @Info        : 
# @Last Edited : 2022-06-12 17:30:37

"""多个坐标系"""
import matplotlib.pyplot as plt
import random


x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(1, 5) for i in x]

# 1. 创建画布
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)

# 2. 绘制图像
axes[0].plot(x, y_shanghai, label="Shanghai")
axes[1].plot(x, y_beijing, label="Beijing", color="r", linestyle="--")

# 添加x,y轴刻度
x_ticks_label = [f"{i}'" for i in x]
y_ticks = range(40)

# 刻度显示
axes[0].set_xticks(x[::5])
axes[0].set_yticks(y_ticks[::5])
axes[0].set_xticklabels(x_ticks_label[::5])
axes[1].set_xticks(x[::5])
axes[1].set_yticks(y_ticks[::5])
axes[1].set_xticklabels(x_ticks_label[::5])

# 添加网格显示
axes[0].grid(True, linestyle="--", alpha=0.5)
axes[1].grid(True, linestyle="--", alpha=0.5)

# 添加描述信息
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Tempreture")
axes[0].set_title("Shanghai Tempreture Change", fontsize=20)
axes[1].set_xlabel("Time")
axes[1].set_ylabel("Tempreture")
axes[1].set_title("Beijing Tempreture Change", fontsize=20)
# 图像保存
plt.savefig("test2.png")

# 添加图例
axes[0].legend(loc=0)
axes[1].legend(loc=0)

# 图像显示
plt.show()
