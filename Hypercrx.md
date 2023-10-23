## 使用Hypercrx插件观察开源社区活动与指标数据

查看OpenLeaderboard发现微软活跃度位居世界第一。接下来使用Hypercrx插件观察microsoft的vscode仓库。
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/dadf0951-56db-4eec-a3ca-c54d1e0e102b)

在edge上下载Hypercrx拓展。打开vscode仓库。
### 活跃度与OpenRank趋势
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/28ae5697-9e0b-445a-9e00-7df8429cf107)

通过该图片可知该仓库自从2015年12月创建以来，前2年内活跃度快速增长，2018年后逐渐保持平稳。而vscode正是在2015年4月首次发布的。

### Issue 创建、关闭和评论事件
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/40801144-9f84-4852-85cd-371305a8f2dc)

可以看出从2019年末到2020年初相关评论的数量达到峰值，而近两年的评论数量有所减少。

### PR 创建、合入和 Review 评论事件&通过 PR 合入增加和删除的代码行数
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/6f669a35-1d87-4dca-ac88-0e827f430b3f)

从2016年到2022年pull requests的增长十分缓慢，而2022年一年pull requests的数量出现了巨幅增长，同时2022年的代码改动行数也是最多的。猜测其原因是vscode在这一年进行了许多更新和改进。

参考其[更新日志](https://code.visualstudio.com/updates/v1_64)可知主要进行了以下更新：

#### 2022年1月（版本1.64）：

新的侧面板：可以同时显示更多的视图。

设置编辑器搜索：现在优先整个单词匹配。

音频提示：当光标移动到折叠区域、错误和断点时，会发出声音。

Unicode高亮：避免在支持的语言中高亮字符。

自动终端回复：为常见的终端提示创建自动响应。

#### 2022年6月（版本1.69）：

3方合并编辑器：在VS Code内解决合并冲突。

命令中心：新的UI，用于搜索文件、运行命令和导航光标历史。

免打扰模式：静音非关键通知弹出窗口。

切换亮/暗主题：快速切换首选的亮和暗主题。

### 贡献者活跃度滚榜
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/27ae11a6-81f4-4dab-9a2c-87ecf2cf3c5e)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/9d650a0c-57ab-4b8f-a893-ae9e208dda57)

观察[活跃度滚榜](https://github.com/microsoft/vscode/pulse?redirect=perceptor)，发现在早期bpasero稳居第一，而后来被VSCodeTriageBot取代。(证明人再卷也卷不过机器)

[bpasero](https://github.com/bpasero)(Benjamin Pasero)正是VScode创始人之一。

### 项目关系网络图
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/57e919d4-71aa-4366-92f1-3584a9fa7d60)

可以看到微软图标几乎占据了整张图片(毕竟是微软自己的软件)。其中最大的一个：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/3462eeef-61ce-4719-8a54-052834779b4a)

### 项目活跃开发者协作网络图
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/cde8e79d-2801-47e4-8d62-56118569eedc)

图标最大的两位正是活跃度滚榜上的两位常胜将军。

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/575a0513-8431-4520-b7dc-dfd36e3040ca)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/2e53817b-1a3f-40a5-a3a7-5af413fcf3d2)
