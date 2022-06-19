#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-09 09:48:25
# @Author      : junsircoding@gmail.com
# @File        : 08-Tensorflow/02-pro/02-线性回归面向对象2.py
# @Info        : 
# @Last Edited : 2022-06-19 21:07:34

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


class MyLinearRegression:
    """
    自实现线性回归

    | 类型 | 实例 |
    | -- | -- |
    | 标量运算 | `tf.add()`, `tf.sub()`, `tf.mul()`, `tf.div()`, `tf.exp()`, `tf.log()`, `tf.greater()`, `tf.less()`, `tf.equal()` |
    | 向量运算 | `tf.concat()`, `tf.slice()`, `tf.splot()`, `tf.constant()`, `tf.rank()`, `tf.shape()`, `tf.shuffle()` |
    | 矩阵运算 | `tf.matmul()`, `tf.matrixinverse()`, `tf.matrixdateminant()` |
    | 带状态的运算 | `tf.Variable()`, `tf.assgin()`, `tf.assginadd()` |
    | 神经网络组件 | `tf.softmax()`, `tf.sigmoid()`, `tf.relu()`, `tf.convolution()`, `tf.max_pool()` |
    | 存储, 恢复 | `tf.train.Saver().save()`, `tf.train.Saver().restore()` |
    | 队列及同步运算 | Enqueue, Dequeue, MutexAcquire, MutexRelease |
    | 控制流 | Merge, Switch, Enter, Leave, NextIteration |

    tf.add(): 
    """

    def __init__(self):
        self.model_path = "./linear_regression/"  # 模型存放目录
        self.log_path = "./summary/"  # 训练日志存放目录, 供 Tensorboard 使用
        self.epoch_times = 1000  # 训练周期次数
        self.tensorboard_cli = f'tensorboard --logdir="{self.log_path}" --host 127.0.0.1 --port 8089'

    def test_inputs(self) -> tuple:
        """测试时使用的输入数据

        tf.random_normal: 从正态分布中输出随机值
        - shape: 张量形状
        - mean: 正态分布的均值
        - stddev: 正态分布的标准差
        - name: 操作的名称

        tf.matmul: 矩阵相乘

        Returns:
            (tuple): x 矩阵, y 矩阵
        """
        test_weight = [[0.2]]  # 初始权重
        test_bias = [[0.6]]  # 初始偏置
        with tf.variable_scope("original_data"):
            # 从正态分布中输出随机值
            test_input = tf.random_normal(
                shape=(100, 1), mean=2,
                stddev=2, name="test_input"
            )
            # 矩阵 test_input 乘以 test_weight
            test_output = tf.matmul(test_input, test_weight) + test_bias
        return test_input, test_output

    def prediction(self, test_input: tf.Tensor) -> tf.Tensor:
        """根据输入数据建立模型

        Args:
            test_input(tf.Tensor): x 源数据张量
        Returns:
            (tf.Tensor): y 预测张量
        """
        with tf.variable_scope("linear_model"):
            # 随机生成权重值
            self.weight = tf.Variable(
                initial_value=tf.random_normal(
                    shape=(1, 1), mean=0.0,
                    stddev=1.0
                ),
                trainable=True,
                name="weight"
            )
            # 随机生成偏置值
            self.bias = tf.Variable(
                initial_value=tf.random_normal(
                    shape=(1, 1), mean=0.0,
                    stddev=1.0
                ),
                trainable=True,
                name="bias"
            )
            # 预测函数
            predict_output = tf.matmul(test_input, self.weight) + self.bias
        return predict_output

    def loss(self, test_output: tf.Tensor, predict_output: tf.Tensor) -> tf.Tensor:
        """目标值和真实值计算损失

        tf.reduce_mean: 张量的各个维度的元素平均值

        tf.square: 求平方

        Returns:
            (tf.Tensor): 损失张量
        """
        with tf.variable_scope("loss"):
            loss = tf.reduce_mean(
                input_tensor=tf.square(predict_output - test_output)
            )
        return loss

    def optimizer(self, loss: tf.Tensor) -> tf.Operation:
        """获取训练OP

        tf.train.GradientDescentOptimizer: 梯度下降优化
        - learning_rate: 学习率, 一般为 0~1 之间比较小的值. 
                         学习率越大, 训练到较好结果的步数越小;
                         学习率越小, 训练到较好结果的步数越大.
                         学习过大会出现梯度爆炸现象

        Args:
            loss(tf.Tensor): 损失张量
        Returns:
            (tf.Operation): 训练 Operation
        """
        with tf.variable_scope("optimizer"):
            optimizer = tf.train.GradientDescentOptimizer(
                learning_rate=0.01).minimize(loss)
        return optimizer

    def merge_summary(self, loss: tf.Tensor) -> tf.Tensor:
        """合并概要

        tf.summary.scalar(name="", tensor): 收集对于损失函数和准确率等单值变量, name 为变量的名字, tensor 为值
        tf.summary.histogram(name="", tensor): 收集高维度的变量参数
        tf.summary.image(name="", tensor): 收集输入的图片张量能显示图片

        Args:
            loss(tf.Tensor): 损失张量
        Returns:
            (tf.Tensor): 合并后的张量
        """
        # 1、生成 TensorBoard 可用的统计日志
        tf.summary.scalar("loss", loss) # 损失函数中的标量值
        tf.summary.histogram("weight", self.weight) # 权重直方图
        tf.summary.histogram("bias", self.bias) # 偏置直方图
        # 2、合并变量
        return tf.summary.merge_all()

    def train(self) -> None:
        """训练模型
        """
        # 获取默认图
        g = tf.get_default_graph()
        # 进入图上下文
        with g.as_default():
            # 训练输入数据
            test_input, test_output = self.test_inputs()
            # 构建神经网络
            predict_output = self.prediction(test_input)
            # 损失函数
            loss_func = self.loss(test_output, predict_output)
            # 优化函数
            optim_func = self.optimizer(loss_func)
            # 收集摘要
            merged = self.merge_summary(loss_func)
            # 初始化模型保存对象
            saver = tf.train.Saver()
            # 开启 tf 会话
            with tf.Session() as sess:
                # 初始化图中的变量
                sess.run(tf.global_variables_initializer())
                print(
                    f"Init random weight: {self.weight.eval()}, random bias: {self.bias.eval()}")
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
                # 训练的步数(依据模型大小而定)
                for epoch in range(self.epoch_times):
                    """
                    因为前面定义了优化函数, 因此随着一轮一轮地训练, 损失值会无限接近 0, 预测出来的权重和偏置会越来越接近测试的输入值
                    """
                    sess.run(optim_func)
                    print(
                        f"Epoch {epoch+1:2}: weight: {self.weight.eval()}, bias: {self.bias.eval()}, loss: {loss_func.eval()}. Summary merged. Summary writed.")
                    # 运行收集变量的结果
                    summary = sess.run(merged)
                    # 添加到文件
                    file_writer.add_summary(summary, epoch)
                    if (epoch+1) % 100 == 0:
                        # 保存的是会话当中的变量 op 值，其他 op 定义的值不保存
                        saver.save(sess, self.model_path)
                        print(f"Epoch {epoch+1}: Operation saved.")


if __name__ == '__main__':
    lr = MyLinearRegression()
    lr.train()
    print(lr.tensorboard_cli)
