#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-09 09:48:25
# @Author      : junsircoding@gmail.com
# @File        : 08-Tensorflow/02-pro/02-线性回归面向对象2.py
# @Info        : 
# @Last Edited : 2022-06-13 11:11:05

"""
+------------------+     +-----------------+     +-------+
| Question, Answer | --> | Algorithm.train | --> | Model |
+------------------+     +-----------------+     +-------+

+-------------+     +---------------+     +-----------+
| NewQuestion | --> | Model.predict | --> | NewAnswer |
+-------------+     +---------------+     +-----------+
"""

# 使用 tensorflow 1.x
import tensorflow._api.v2.compat.v1 as tf
import os
# 关闭 tf 的警告日志
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.logging.set_verbosity(tf.logging.ERROR)
# 关闭 eager execution
tf.disable_eager_execution()


class MyLinearRegression(object):
    """
    自实现线性回归
    """

    def __init__(self):
        self.model_path = "08-Tensorflow/02-pro/linear_regression/"
        self.log_path = "08-Tensorflow/02-pro/summary/"
        self.max_step = 100
        self.tensorboard = f'tensorboard --logdir="{self.log_path}" --host 127.0.0.1 --port 8089'

    def inputs(self):
        """获取特征值目标值数据

        Returns:
            (tuple): x 矩阵, y 矩阵
        """
        with tf.variable_scope("original_data"):
            x_data = tf.random_normal(
                [100, 1], mean=1.0, stddev=1.0, name="x_data")
            y_true = tf.matmul(x_data, [[0.7]]) + 0.8
        return x_data, y_true

    def inference(self, feature):
        """根据输入数据建立模型

        Args:
            feature(tf.Tensor): x 源数据张量
        Returns:
            (tf.Tensor): y 预测张量
        """
        with tf.variable_scope("linear_model"):
            self.weight = tf.Variable(tf.random_normal([1, 1], mean=0.0, stddev=1.0),
                                      name="weights")
            self.bias = tf.Variable(0.0, name='biases')
            y_predict = tf.matmul(feature, self.weight) + self.bias
        return y_predict

    def loss(self, y_true, y_predict):
        """目标值和真实值计算损失

        Returns:
            (tf.Tensor): 损失张量
        """
        with tf.variable_scope("loss"):
            loss = tf.reduce_mean(tf.square(y_predict - y_true))
        return loss

    def merge_summary(self, loss):
        """合并概要

        Args:
            loss(tf.Tensor): 损失张量
        Returns:
            (tf.Tensor): 合并后的张量
        """
        # 1、收集张量的值
        tf.summary.scalar("losses", loss)
        tf.summary.histogram("weights", self.weight)
        tf.summary.histogram('bias', self.bias)
        # 2、合并变量
        return tf.summary.merge_all()

    def sgd_op(self, loss):
        """获取训练OP

        Args:
            loss(tf.Tensor): 损失张量
        Returns:
            (tf.Operation): 训练 Operation
        """
        with tf.variable_scope("optimizer"):
            optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
        return optimizer

    def train(self):
        """训练模型
        """
        g = tf.get_default_graph()
        with g.as_default():
            x_data, y_true = self.inputs()
            y_predict = self.inference(x_data)
            loss = self.loss(y_true, y_predict)
            train_op = self.sgd_op(loss)
            # 收集观察的结果值
            merged = self.merge_summary(loss)
            saver = tf.train.Saver()
            with tf.Session() as sess:
                sess.run(tf.global_variables_initializer())
                # 在没训练，模型的参数值
                print("初始化的权重：%f, 偏置：%f" %
                      (self.weight.eval(), self.bias.eval()))
                # 加载模型
                checkpoint = os.path.exists(f"./{self.model_path}/checkpoint")
                print(f"checkpoint: {checkpoint}")
                if checkpoint:
                    print('Restoring', self.model_path)
                    saver.restore(sess, self.model_path)
                # 生成事件文件，观察图结构
                file_writer = tf.summary.FileWriter(
                    self.log_path, graph=sess.graph)
                # 开启训练
                # 训练的步数（依据模型大小而定）
                for epoch in range(self.max_step):
                    sess.run(train_op)
                    print("\r" + "训练第%d步之后的损失:%f, 权重：%f, 偏置：%f" % (
                        epoch,
                        loss.eval(),
                        self.weight.eval(),
                        self.bias.eval()),
                        end="",
                        flush=True)
                    # 运行收集变量的结果
                    summary = sess.run(merged)
                    # 添加到文件
                    file_writer.add_summary(summary, epoch)
                    if epoch % 100 == 0:
                        # 保存的是会话当中的变量op值，其他op定义的值不保存
                        saver.save(sess, self.model_path)


if __name__ == '__main__':
    lr = MyLinearRegression()
    lr.train()
    print()
    print(lr.tensorboard)
