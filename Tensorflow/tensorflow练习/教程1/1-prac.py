#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : Tensorflow/tensorflow练习/教程1/1-prac.py
# @Info        : 
# @Last Edited : 2022-06-07 10:59:16

"""
tensorflow 练习
API: https://www.tensorflow.org/api_docs/python/tf
"""

import tensorflow as tf

# MNIST 模块
mnist = tf.keras.datasets.mnist

# 调用 load_data 方法, 加载 MNIST 数据集到 `~/.keras/datasets/` 目录
(x_train, y_train), (x_test, y_test) = mnist.load_data()
"""
x_train: uint8 NumPy 灰度图像数据数组, 形状为 (60000, 28, 28), 包含训练数据. 像素值范围从 0 到 255.
y_train: uint8 NumPy 数字标签数组 (0-9 范围内的整数）, 形状为 (60000,), 用于训练数据.
x_test: uint8 NumPy 灰度图像数据数组, 形状为 (10000, 28, 28), 包含测试数据. 像素值范围从 0 到 255.
y_test: uint8 NumPy 数字标签数组 (0-9 范围内的整数）, 形状为 (10000,), 用于测试数据.
"""

# 将样本从整数转换为浮点数
x_train, x_test = x_train / 255.0, x_test / 255.0

# 将模型的各层堆叠起来, 以搭建 tf.keras.Sequential 模型.
"""
Sequential 将层的线性堆栈分组到 tf.keras.Model 中.
"""
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# 为训练选择优化器和损失函数: 
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 训练模型
model.fit(x_train, y_train, epochs=5)

# 验证模型
model.evaluate(x_test,  y_test, verbose=2)
