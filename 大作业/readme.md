# 探究NBA球员选秀顺位与成才之间的关系
## 前言
作为NBA招募新球员的方式，每年现场直播的梦幻选秀都是其最大看点之一。我们可能会感到疑惑：选秀顺位高(低)是否一定代表球员水平高(低)？顺位高低与球员是否成才之间又有怎样的关系？本次研究将通过对1989-2021年NBA选秀球员的比赛数据，球场表现等方面进行分析，揭示球员职业生涯与其初入联盟时的选秀顺位间的内在联系。以此为球队在考虑选择新秀球员时提供参考与建议，同时提升大家对NBA的理解深度和预测水平，帮助大家成为懂球帝(。
## 研究对象和方法
本次研究的数据集:[nbaplayersdraft](https://github.com/litterqi/Introduction-to-data-science-and-engineering/blob/%E4%BD%9C%E4%B8%9A/%E5%A4%A7%E4%BD%9C%E4%B8%9A/nbaplayersdraft.csv) 来源:[kaggle](https://www.kaggle.com/datasets/mattop/nba-draft-basketball-player-data-19892021/)

研究过程中会用到的数据科学方法，包括：

1.数据清洗(Data Cleaning) 在进行数据分析前对原始数据进行处理和修复，消除数据中的噪声、错误、缺失值和不一致性，以提高数据质量和可靠性。

2.数据可视化(Data Visualization) 将数据和信息转化为图表、表格、图像等可视化形式，以便更容易地理解和分析数据。

3.探索性数据分析(Exploratory Data Analysis) 通过可视化和统计技术来探索数据集的特征、结构和关系，发现其中的模式、趋势、异常值和关联性。

4.机器学习(Machine Learning) 通过对已有数据进行分析、挖掘和模式识别，从中提取出规律和知识。

5.聚类(Clustering) 将数据集中的样本按照相似性进行分组或聚集，发现数据中的内在模式和结构。
