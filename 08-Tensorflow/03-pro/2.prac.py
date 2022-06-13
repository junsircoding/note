#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 08-Tensorflow/03-pro/2.prac.py
# @Info        : 
# @Last Edited : 2022-06-13 11:11:05

"""
TensorFlow 程序的快速概述
训练一个神经网络模型, 对运动鞋和衬衫等服装图像进行分类.
"""

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)  # tensorflow 版本

"""
导入 Fashion MNIST 数据集.
该数据集包含 10 个类别的 70,000 个灰度图像.
这些图像以低分辨率(28x28 像素)展示了单件衣物.

Fashion MNIST 旨在临时替代经典 MNIST 数据集, 后者常被用作计算机视觉机器学习程序的“Hello, World”.
MNIST 数据集包含手写数字 (0、1、2 等) 的图像, 其格式与您将使用的衣物图像的格式相同.

本指南使用 Fashion MNIST 来实现多样化, 因为它比常规 MNIST 更具挑战性.
这两个数据集都相对较小, 都用于验证某个算法是否按预期工作.
对于代码的测试和调试, 它们都是很好的起点.

在本指南中, 我们使用 60,000 个图像来训练网络, 使用 10,000 个图像来评估网络学习对图像分类的准确率.
您可以直接从 TensorFlow 访问 Fashion MNIST.
"""
# Fashion MNIST 模块
fashion_mnist = keras.datasets.fashion_mnist

# 调用 load_data 方法加载数据集到 `~/.keras/datasets/`
"""
train_images 和 train_labels 数组是训练集，即模型用于学习的数据.
测试集、test_images 和 test_labels 数组会被用来对模型进行测试.
"""
(train_images, train_labels), (test_images,
                               test_labels) = fashion_mnist.load_data()

"""
在训练模型之前，我们先浏览一下数据集的格式.以下代码显示训练集中有 60,000 个图像，每个图像由 28 x 28 的像素表示
"""
print(
    f"Fashion MNIST 数据训练集结构为: {train_images.shape}, 有 {len(train_labels)} 个标签")
print(f"Fashion MNIST 数据测试集结构为: {test_images.shape}, 有 {len(test_labels)} 个标签")

"""
预处理数据
在训练网络之前，必须对数据进行预处理.
如果您检查训练集中的第一个图像，您会看到像素值处于 0 到 255 之间：
"""
# plt.figure()
# plt.imshow(train_images[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()

"""
将这些值缩小至 0 到 1 之间，然后将其馈送到神经网络模型.
为此，请将这些值除以 255.请务必以相同的方式对训练集和测试集进行预处理：
"""
train_images = train_images / 255.0
test_images = test_images / 255.0

"""
为了验证数据的格式是否正确，以及您是否已准备好构建和训练网络，让我们显示训练集中的前 25 个图像，并在每个图像下方显示类名称.
每个图像都会被映射到一个标签
"""
# class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
#                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# plt.figure(figsize=(10, 10))
# for i in range(25):
#     plt.subplot(5, 5, i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i], cmap=plt.cm.binary)
#     plt.xlabel(class_names[train_labels[i]])
# plt.show()

"""
构建模型
构建神经网络需要先配置模型的层，然后再编译模型.

设置层
神经网络的基本组成部分是层.
层会从向其馈送的数据中提取表示形式.希望这些表示形式有助于解决手头上的问题.
大多数深度学习都包括将简单的层链接在一起.
大多数层(如 tf.keras.layers.Dense)都具有在训练期间才会学习的参数.
"""

"""
该网络的第一层 tf.keras.layers.Flatten 将图像格式从二维数组(28 x 28 像素）转换成一维数组(28 x 28 = 784 像素）.
将该层视为图像中未堆叠的像素行并将其排列起来.
该层没有要学习的参数，它只会重新格式化数据.
展平像素后，网络会包括两个 tf.keras.layers.Dense 层的序列.它们是密集连接或全连接神经层.
第一个 Dense 层有 128 个节点(或神经元）.
第二个(也是最后一个）层会返回一个长度为 10 的 logits 数组.
每个节点都包含一个得分，用来表示当前图像属于 10 个类中的哪一类.
"""
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])

"""
编译模型
在准备对模型进行训练之前，还需要再对其进行一些设置。以下内容是在模型的编译步骤中添加的：
损失函数 - 用于测量模型在训练期间的准确率。您会希望最小化此函数，以便将模型“引导”到正确的方向上。
优化器 - 决定模型如何根据其看到的数据和自身的损失函数进行更新。
指标 - 用于监控训练和测试步骤。以下示例使用了准确率，即被正确分类的图像的比率。
"""
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

"""
训练模型

训练神经网络模型需要执行以下步骤：

将训练数据馈送给模型。在本例中，训练数据位于 train_images 和 train_labels 数组中。
模型学习将图像和标签关联起来。
要求模型对测试集（在本例中为 test_images 数组）进行预测。
验证预测是否与 test_labels 数组中的标签相匹配。
"""
model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)

"""
结果表明，模型在测试数据集上的准确率略低于训练数据集。
训练准确率和测试准确率之间的差距代表过拟合。
过拟合是指机器学习模型在新的、以前未曾见过的输入上的表现不如在训练数据上的表现。
过拟合的模型会“记住”训练数据集中的噪声和细节，从而对模型在新数据上的表现产生负面影响。
有关更多信息，请参阅以下内容：
"""

"""
进行预测
在模型经过训练后，您可以使用它对一些图像进行预测。模型具有线性输出，即 logits。您可以附加一个 softmax 层，将 logits 转换成更容易理解的概率。
"""
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(test_images)
"""
在上例中，模型预测了测试集中每个图像的标签。我们来看看第一个预测结果：
"""
print(predictions[0])
"""
预测结果是一个包含 10 个数字的数组。它们代表模型对 10 种不同服装中每种服装的“置信度”。您可以看到哪个标签的置信度值最大：
"""
print(np.argmax(predictions[0]))
