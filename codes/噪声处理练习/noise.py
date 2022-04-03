import numpy as np
import matplotlib.pyplot as plt


def add_gaussian_noise(pc: np.ndarray, sigma: float, clip: float):
    """
    将给定均值和标准差的高斯噪声添加到点云
    :param pc: B X N X 3 array, original batch of point clouds
    :param sigma: mean of noise
    :param clip: standard deviation of noise
    :return: point cloud with noise
    """
    pc_shape = pc.shape
    # 生成噪声数据
    jittered_data = np.clip(
        sigma * np.random.randn(*pc_shape), -1 * clip, clip)
    # 将噪声数据与原始数据合并
    jittered_data += pc
    return jittered_data


def draw():
    fig = plt.figure()

    source_data = np.load('./85.npy')
    x1 = source_data[:, 0]
    y1 = source_data[:, 1]
    z1 = source_data[:, 2]
    ax = fig.add_subplot(1, 2, 1, projection='3d')

    merged_data = np.load('./noise_85.npy')
    x2 = merged_data[:, 0]
    y2 = merged_data[:, 1]
    z2 = merged_data[:, 2]
    # ax2 = fig.add_subplot(1, 2, 1, projection='3d')

    ax.scatter(x1, y1, z1, s=3, c='b', depthshade=True, marker='o')
    ax.scatter(x2, y2, z2, s=1, c='r', depthshade=True, marker='o')
    plt.axis("off")
    plt.xticks([])
    plt.yticks([])
    plt.show()


if __name__ == '__main__':
    # 显示源数据
    # # 读取源数据
    source_data = np.load('./85.npy')
    # # 生成噪声数据
    merged_data = add_gaussian_noise(source_data, 10, 0.5)
    np.save('noise_85.npy', merged_data)
    # 显示图像
    draw()
