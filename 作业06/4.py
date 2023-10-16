import numpy as np
A = np.array([[2, 1], [4, 5]])
n = A.shape[0] # 矩阵A的维数
x = np.random.randn(n) # 初始化x
max_iter = 1000 # 最大迭代次数
tol = 1e-6 # 收敛阈值
for i in range(max_iter):
    y = np.dot(A, x) # 计算y = Ax
    lmd = np.dot(x, y) / np.dot(x, x) # 计算lmd
    err = np.linalg.norm(y - lmd * x) # 计算误差
    if err < tol:
        break
    x = y / np.linalg.norm(y) # 更新x
print('矩阵 A 的最大特征值为：', lmd)