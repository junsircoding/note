#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding@gmail.com
# @File        : 08-Tensorflow/02-pro/tf实现线性回归.py
# @Info        : 
# @Last Edited : 2022-06-14 22:22:27

"""
Shift + Command + P: python:launch tensorboard
tensorboard --logdir="./summary" --host 127.0.0.1 --port 8089
"""

import tensorflow._api.v2.compat.v1 as tf
import os
# 关闭 tf 的警告日志
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.logging.set_verbosity(tf.logging.ERROR)
# 使用 tensorflow 1.x
"""
官方更推荐 `import tensorflow.compat.v1 as tf` 来导入 1.x 版本的 tf
但是编辑器无法提示代码, 体验不好
阅读源码后, 发现其实质是从 _api 导入
"""

# 关闭 eager execution
tf.disable_eager_execution()

MODEL_PATH = "./linear_regression/"


def linear_regression():
    """
    准备源输入数据和他们套公式之后的正确答案
    源输入数据是 x
    导公式之后的正确答案是 y_true
    他们都是 100x1 的一维矩阵
    """
    with tf.variable_scope("original_data"):
        x = tf.random_normal(shape=(100, 1), mean=2, stddev=2)
        y_true = tf.matmul(x, [[0.8]]) + 0.7

    """
    建立线性模型：
    y = weights * x + bias
    目标: 求出权重 weights 和偏置 bias
    随机初始化 weights 和 bias
    """
    with tf.variable_scope("linear_model"):
        weights = tf.Variable(initial_value=tf.random_normal(shape=(1, 1)))
        bias = tf.Variable(initial_value=tf.random_normal(shape=(1, 1)))
        y_predict = tf.matmul(x, weights) + bias

    """
    确定损失函数(预测值与真实值之间的误差)-均方误差
    """
    with tf.variable_scope("loss"):
        loss = tf.reduce_mean(tf.square(y_predict - y_true))

    """
    梯度下降优化损失：需要指定学习率(超参数)
    weights_2 = weights_1 - 学习率*(方向)
    bias_2 = bias_1 - 学习率*(方向)
    """
    with tf.variable_scope("gd_optimizer"):
        optimizer = tf.train.GradientDescentOptimizer(
            learning_rate=0.01).minimize(loss)

    # 收集变量
    tf.summary.scalar("loss", loss)
    tf.summary.histogram("weights", weights)
    tf.summary.histogram("bias", bias)
    # 合并变量
    merge = tf.summary.merge_all()
    # 初始化变量
    init = tf.global_variables_initializer()
    # 创建saver对象
    saver = tf.train.Saver()

    # 开启会话进行训练
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init)
        print("随机初始化的权重为[%f], 偏置为[%f]" % (weights.eval(), bias.eval()))
        # 当存在 checkpoint 文件，就加载模型
        if os.path.exists(f"./{MODEL_PATH}/checkpoint"):
            saver.restore(sess, MODEL_PATH)
        # 创建概括文件, 供 tensorboard 使用
        file_writer = tf.summary.FileWriter(
            logdir="./summary", graph=sess.graph)
        # 训练模型
        for epoch in range(100):
            sess.run(optimizer)
            print(
                "\r" +
                f"第[{epoch:2}]步的误差为[{loss.eval()}], 权重为{weights.eval()}, 偏置为{bias.eval()}",
                end="",
                flush=True
            )
            # 合并变量
            summary = sess.run(merge)
            # 记录日志
            file_writer.add_summary(summary, epoch)
            # 每 10 次记录记录一次模型
            if epoch % 10 == 0:
                saver.save(sess, MODEL_PATH)
    return None


def main(argv):
    linear_regression()


if __name__ == "__main__":
    tf.app.run()
