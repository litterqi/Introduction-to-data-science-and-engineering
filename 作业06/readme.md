# 第六周作业
## 第十章：

### 第1题：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/cfd6ab51-5d54-4503-8f31-5bb6454bcc60)

### 第2题：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/5720e64c-c35f-4e7e-b57e-35613e5b3072)

### 第3题：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/afd3ad61-c53e-4471-b04a-aa356d4ec8e0)

### 第4题：

我们首先定义了矩阵 A ，最大迭代次数 max_iter 和收敛阈值 tol。然后我们使用随机向量初始化 x，并通过 for 循环开始执行编程幂迭代法。在每个迭代步骤中，我们计算 y = Ax 和特征值 lmd，并计算误差 err。如果误差小于指定的收敛阈值 tol，则结束循环。否则更新 x，继续迭代。最后，我们输出计算出的最大特征值 lmd。

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/25be7386-6b5d-4295-8fbd-4e75ef295204)

### 第5题：

我们使用numpy的cov函数来计算协方差矩阵。参数data是包含原始数据的矩阵。当`bias=True`时，np.cov函数会采用无偏估计来计算样本协方差矩阵。在无偏估计中，分母为 n−1，其中 
n表示样本量。这种计算方法可以更好地反映样本之间的关系，因为它减少了在统计学上可能出现的偏差。但是，对于较小的样本量，由于减去了自由度的数量，可能会导致方差估计偏低，从而影响协方差矩阵的准确性。

当`bias=False`时，np.cov 函数会采用有偏估计来计算样本协方差矩阵。在有偏估计中，分母为 n，不需要减去自由度的数量，但是会将样本方差略微高估，可能会导致比无偏估计稍微错误的协方差矩阵。

cov函数返回计算得到的协方差矩阵C。

`bias=True`情况下的结果为：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/f5e7f8c5-ef42-4092-b2aa-3b923e1b7ed8)

`bias=False`情况下的结果为：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/a8f4cf6d-9eb0-4f9b-8415-05df6dd6b61b)

### 第6题：
上一题`bias=True`情况下的结果为：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/9e14b5f1-7833-42a1-9528-f4d148c07645)

上一题`bias=False`情况下的结果为：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/8d7f363f-23b5-458e-adfc-5eca9c9fddd1)
