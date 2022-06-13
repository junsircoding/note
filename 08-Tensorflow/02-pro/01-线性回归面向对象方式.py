#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-09 09:24:50
# @Author      : junsircoding@gmail.com
# @File        : 08-Tensorflow/02-pro/01-线性回归面向对象方式.py
# @Info        : 
# @Last Edited : 2022-06-13 11:11:05

# 使用 tensorflow 1.x
import tensorflow._api.v2.compat.v1 as tf
import os
# 关闭 tf 的警告日志
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.logging.set_verbosity(tf.logging.ERROR)
# 关闭 eager execution
tf.disable_eager_execution()


class LinerRegression:
    """线性回归模型"""

    def __init__(self):
        self.model_path = "08-Tensorflow/02-pro/linear_regression/"
        self.log_path = "08-Tensorflow/02-pro/summary/"

    def add_varible(self):
        with tf.variable_scope("original_data"):
            x = tf.random_normal(shape=(100, 1), mean=2, stddev=2)
            y_true = tf.matmul(x, [[0.8]]) + 0.7
        with tf.variable_scope("linear_model"):
            weights = tf.Variable(initial_value=tf.random_normal(shape=(1, 1)))
            bias = tf.Variable(initial_value=tf.random_normal(shape=(1, 1)))
            y_predict = tf.matmul(x, weights) + bias
        with tf.variable_scope("loss"):
            loss = tf.reduce_mean(tf.square(y_predict - y_true))
        with tf.variable_scope("gd_optimizer"):
            optimizer = tf.train.GradientDescentOptimizer(
                learning_rate=0.01).minimize(loss)
        # 收集变量
        tf.summary.scalar("loss", loss)
        tf.summary.histogram("weights", weights)
        tf.summary.histogram("bias", bias)
        # 合并变量
        merge = tf.summary.merge_all()
        return loss, weights, bias, optimizer, merge

    def train(self):
        loss, weights, bias, optimizer, merge = self.add_varible()
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
            if os.path.exists(f"./{self.model_path}/checkpoint"):
                saver.restore(sess, self.model_path)
            # 创建概括文件, 供 tensorboard 使用
            file_writer = tf.summary.FileWriter(
                logdir=self.log_path, graph=sess.graph)
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
                    saver.save(sess, self.model_path)

if __name__ == "__main__":
    linear_regression =  LinerRegression()
    linear_regression.train()
