# 第二周作业
## 第一题：

(1) 解决这个问题的第一步是观察到当 n > 5 时，所求的正整数列是由多个 3 组成的，以及一个余数 n % 3。

(2) 由柯西不等式可知，将某个数n分割成k个数，讨论这k个数的乘积时，乘积的最大值总出现在将n等分成k个数的时候。知道了这一点以后，发现其最大值在x=e处取得。但是由于x是正整数，最大值只能是当x=2或x=3时取到。使用程序进行实验，将每个数分成若干个 2 或 3 或这两个数的混合时，得到当n=2001时，所求的正整数列是 3, 3, ..., 3，共有 667 个 3。

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/56970516-a6ad-4546-afb1-06f92e1020b0)

## 第二题：
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/4bca5fa9-ba0c-4f75-afd6-65009d3c3ce3)

## 第三题：
这题是关于‘人’，‘狼’，‘羊’，‘菜’代表的节点构成的图论问题。使用深度优先搜索算法查找图中所有可能的路径。

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/386a169d-a7d7-4a8b-a680-9da796b87896)

## 第四题：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/416201f3-3594-4ecf-a192-60def425eb95)

## 第五题：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/d2b27197-e3be-4608-842e-9d0afff1fd06)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/af8a5685-eca8-4bb9-80cc-9d4229b8569f)

## 第六题：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/c02fcc3a-7fcf-4f14-826d-5dc1e51c9a0c)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/e2d63a7e-74c0-45f8-a3d0-6b9bff2e47c7)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/50b8e098-955d-44f0-a20a-03b9be27790e)

## 第七题：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/e8b1bec7-ab17-4009-84e9-11afdca238bf)

## 第八题：

方法一：使用 Leibniz 公式(泰勒展开)计算圆周率

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/6bc34c25-73d3-402e-90e8-4c229d48a281)

方法二：使用 acos() 函数计算圆周率

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/dd0b7f1d-57fb-43b5-9a4e-29d211718305)

方法三：使用随机投针法(蒙特卡洛法)计算圆周率

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/78bb1423-91c9-4f6b-884a-3901f7eda70a)

可以发现泰勒展开法的效率低于蒙特卡洛法。
## 第九题：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/fda96435-49a1-49c9-82e2-f31e73a56be3)
