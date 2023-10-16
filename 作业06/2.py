import numpy as np
import matplotlib.pyplot as plt
# 生成100个服从标准正态分布的样本
samples = np.random.normal(0, 1, 100)
# 绘制直方图
plt.hist(samples, bins=20, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Samples')
# 显示图表
plt.show()