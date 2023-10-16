import numpy as np
# 构造矩阵 A
A = np.array([[2, 1], [4, 5]])
# 计算特征值和特征向量
eigen_values, eigen_vectors = np.linalg.eig(A)
# 输出结果
print('特征值:\n', eigen_values)
print('特征向量:\n', eigen_vectors)