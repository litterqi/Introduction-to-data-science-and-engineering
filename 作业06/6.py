
import numpy as np

data = np.array([[1, -1, 4],
                 [2, 1, 3],
                 [1, 3, -1]])

C = np.cov(data,bias=True)
eigenvalues, eigenvectors = np.linalg.eig(C)

print("协方差矩阵C的全部特征值:")
print(eigenvalues)

print("协方差矩阵C的全部特征向量:")
print(eigenvectors) 