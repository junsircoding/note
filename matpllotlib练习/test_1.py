"""matplotlib 是专门用于开发2D/3D图表的包"""

import matplotlib.pyplot as plt

# 1. 创建画布
plt.figure(figsize=(10, 10), dpi=100)

# 绘制折线图
plt.plot(
    [1, 2, 3, 4, 5, 6, 7],
    [17, 17, 18, 15, 11, 11, 13]
)

# 显示图像
plt.show()
