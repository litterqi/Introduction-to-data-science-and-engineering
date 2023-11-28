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

## 数据读取
```
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px #graphing
import missingno as msno #describe data
import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/1f9eef49-f66f-4db2-8bbd-b98ba5cd5ec1)

导入numpy，pandas，plotly，missingno等库用于数据处理。使用os库中的walk()函数读取数据集文件。

```
df.dropna()
```

使用dropna()函数从数据集中删除包含任何缺失值的行。

```
df = pd.read_csv("/kaggle/input/nbaplayersdraft.csv")
df.head()
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>year</th>
      <th>rank</th>
      <th>overall_pick</th>
      <th>team</th>
      <th>player</th>
      <th>college</th>
      <th>years_active</th>
      <th>games</th>
      <th>minutes_played</th>
      <th>...</th>
      <th>3_point_percentage</th>
      <th>free_throw_percentage</th>
      <th>average_minutes_played</th>
      <th>points_per_game</th>
      <th>average_total_rebounds</th>
      <th>average_assists</th>
      <th>win_shares</th>
      <th>win_shares_per_48_minutes</th>
      <th>box_plus_minus</th>
      <th>value_over_replacement</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1989</td>
      <td>1</td>
      <td>1</td>
      <td>SAC</td>
      <td>Pervis Ellison</td>
      <td>Louisville</td>
      <td>11.0</td>
      <td>474.0</td>
      <td>11593.0</td>
      <td>...</td>
      <td>0.050</td>
      <td>0.689</td>
      <td>24.5</td>
      <td>9.5</td>
      <td>6.7</td>
      <td>1.5</td>
      <td>21.8</td>
      <td>0.090</td>
      <td>-0.5</td>
      <td>4.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1989</td>
      <td>2</td>
      <td>2</td>
      <td>LAC</td>
      <td>Danny Ferry</td>
      <td>Duke</td>
      <td>13.0</td>
      <td>917.0</td>
      <td>18133.0</td>
      <td>...</td>
      <td>0.393</td>
      <td>0.840</td>
      <td>19.8</td>
      <td>7.0</td>
      <td>2.8</td>
      <td>1.3</td>
      <td>34.8</td>
      <td>0.092</td>
      <td>-0.9</td>
      <td>4.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1989</td>
      <td>3</td>
      <td>3</td>
      <td>SAS</td>
      <td>Sean Elliott</td>
      <td>Arizona</td>
      <td>12.0</td>
      <td>742.0</td>
      <td>24502.0</td>
      <td>...</td>
      <td>0.375</td>
      <td>0.799</td>
      <td>33.0</td>
      <td>14.2</td>
      <td>4.3</td>
      <td>2.6</td>
      <td>55.7</td>
      <td>0.109</td>
      <td>0.2</td>
      <td>13.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1989</td>
      <td>4</td>
      <td>4</td>
      <td>MIA</td>
      <td>Glen Rice</td>
      <td>Michigan</td>
      <td>15.0</td>
      <td>1000.0</td>
      <td>34985.0</td>
      <td>...</td>
      <td>0.400</td>
      <td>0.846</td>
      <td>35.0</td>
      <td>18.3</td>
      <td>4.4</td>
      <td>2.1</td>
      <td>88.7</td>
      <td>0.122</td>
      <td>0.8</td>
      <td>24.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1989</td>
      <td>5</td>
      <td>5</td>
      <td>CHH</td>
      <td>J.R. Reid</td>
      <td>UNC</td>
      <td>11.0</td>
      <td>672.0</td>
      <td>15370.0</td>
      <td>...</td>
      <td>0.135</td>
      <td>0.716</td>
      <td>22.9</td>
      <td>8.5</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>22.5</td>
      <td>0.070</td>
      <td>-2.9</td>
      <td>-3.7</td>
    </tr>
  </tbody>
</table>

使用head()函数显示前5行数据。
## 基本数据统计信息
```
print(df.shape)
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/b7e786c9-0381-477b-ae39-60c3dc553b51)

使用shape属性获得数据集的行数与列数。

```
df.info()
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/38ac6e56-efdd-4909-821f-dac7eb31b853)

使用info()函数获得数据集信息结构。

```
df.describe().style.background_gradient(cmap = "Blues")
```
<table id="T_802a1_">
  <thead>
    <tr>
      <th class="blank level0">&nbsp;</th>
      <th class="col_heading level0 col0">id</th>
      <th class="col_heading level0 col1">year</th>
      <th class="col_heading level0 col2">rank</th>
      <th class="col_heading level0 col3">overall_pick</th>
      <th class="col_heading level0 col4">years_active</th>
      <th class="col_heading level0 col5">games</th>
      <th class="col_heading level0 col6">minutes_played</th>
      <th class="col_heading level0 col7">points</th>
      <th class="col_heading level0 col8">total_rebounds</th>
      <th class="col_heading level0 col9">assists</th>
      <th class="col_heading level0 col10">field_goal_percentage</th>
      <th class="col_heading level0 col11">3_point_percentage</th>
      <th class="col_heading level0 col12">free_throw_percentage</th>
      <th class="col_heading level0 col13">average_minutes_played</th>
      <th class="col_heading level0 col14">points_per_game</th>
      <th class="col_heading level0 col15">average_total_rebounds</th>
      <th class="col_heading level0 col16">average_assists</th>
      <th class="col_heading level0 col17">win_shares</th>
      <th class="col_heading level0 col18">win_shares_per_48_minutes</th>
      <th class="col_heading level0 col19">box_plus_minus</th>
      <th class="col_heading level0 col20">value_over_replacement</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_802a1_level0_row0" class="row_heading level0 row0">count</th>
      <td id="T_802a1_row0_col0" class="data row0 col0">1922.000000</td>
      <td id="T_802a1_row0_col1" class="data row0 col1">1922.000000</td>
      <td id="T_802a1_row0_col2" class="data row0 col2">1922.000000</td>
      <td id="T_802a1_row0_col3" class="data row0 col3">1922.000000</td>
      <td id="T_802a1_row0_col4" class="data row0 col4">1669.000000</td>
      <td id="T_802a1_row0_col5" class="data row0 col5">1669.000000</td>
      <td id="T_802a1_row0_col6" class="data row0 col6">1669.000000</td>
      <td id="T_802a1_row0_col7" class="data row0 col7">1669.000000</td>
      <td id="T_802a1_row0_col8" class="data row0 col8">1669.000000</td>
      <td id="T_802a1_row0_col9" class="data row0 col9">1669.000000</td>
      <td id="T_802a1_row0_col10" class="data row0 col10">1665.000000</td>
      <td id="T_802a1_row0_col11" class="data row0 col11">1545.000000</td>
      <td id="T_802a1_row0_col12" class="data row0 col12">1633.000000</td>
      <td id="T_802a1_row0_col13" class="data row0 col13">1669.000000</td>
      <td id="T_802a1_row0_col14" class="data row0 col14">1669.000000</td>
      <td id="T_802a1_row0_col15" class="data row0 col15">1669.000000</td>
      <td id="T_802a1_row0_col16" class="data row0 col16">1669.000000</td>
      <td id="T_802a1_row0_col17" class="data row0 col17">1669.000000</td>
      <td id="T_802a1_row0_col18" class="data row0 col18">1668.000000</td>
      <td id="T_802a1_row0_col19" class="data row0 col19">1668.000000</td>
      <td id="T_802a1_row0_col20" class="data row0 col20">1669.000000</td>
    </tr>
    <tr>
      <th id="T_802a1_level0_row1" class="row_heading level0 row1">mean</th>
      <td id="T_802a1_row1_col0" class="data row1 col0">961.500000</td>
      <td id="T_802a1_row1_col1" class="data row1 col1">2005.317378</td>
      <td id="T_802a1_row1_col2" class="data row1 col2">29.694589</td>
      <td id="T_802a1_row1_col3" class="data row1 col3">29.694589</td>
      <td id="T_802a1_row1_col4" class="data row1 col4">6.332534</td>
      <td id="T_802a1_row1_col5" class="data row1 col5">348.042540</td>
      <td id="T_802a1_row1_col6" class="data row1 col6">8399.055722</td>
      <td id="T_802a1_row1_col7" class="data row1 col7">3580.413421</td>
      <td id="T_802a1_row1_col8" class="data row1 col8">1497.009587</td>
      <td id="T_802a1_row1_col9" class="data row1 col9">774.300779</td>
      <td id="T_802a1_row1_col10" class="data row1 col10">0.436568</td>
      <td id="T_802a1_row1_col11" class="data row1 col11">0.272405</td>
      <td id="T_802a1_row1_col12" class="data row1 col12">0.716825</td>
      <td id="T_802a1_row1_col13" class="data row1 col13">18.134032</td>
      <td id="T_802a1_row1_col14" class="data row1 col14">7.275734</td>
      <td id="T_802a1_row1_col15" class="data row1 col15">3.194368</td>
      <td id="T_802a1_row1_col16" class="data row1 col16">1.550749</td>
      <td id="T_802a1_row1_col17" class="data row1 col17">17.873697</td>
      <td id="T_802a1_row1_col18" class="data row1 col18">0.061691</td>
      <td id="T_802a1_row1_col19" class="data row1 col19">-2.311271</td>
      <td id="T_802a1_row1_col20" class="data row1 col20">4.403176</td>
    </tr>
    <tr>
      <th id="T_802a1_level0_row2" class="row_heading level0 row2">std</th>
      <td id="T_802a1_row2_col0" class="data row2 col0">554.977927</td>
      <td id="T_802a1_row2_col1" class="data row2 col1">9.456946</td>
      <td id="T_802a1_row2_col2" class="data row2 col2">16.912454</td>
      <td id="T_802a1_row2_col3" class="data row2 col3">16.912454</td>
      <td id="T_802a1_row2_col4" class="data row2 col4">4.656321</td>
      <td id="T_802a1_row2_col5" class="data row2 col5">324.897567</td>
      <td id="T_802a1_row2_col6" class="data row2 col6">9845.871529</td>
      <td id="T_802a1_row2_col7" class="data row2 col7">4826.142847</td>
      <td id="T_802a1_row2_col8" class="data row2 col8">2003.686388</td>
      <td id="T_802a1_row2_col9" class="data row2 col9">1284.602969</td>
      <td id="T_802a1_row2_col10" class="data row2 col10">0.083846</td>
      <td id="T_802a1_row2_col11" class="data row2 col11">0.128339</td>
      <td id="T_802a1_row2_col12" class="data row2 col12">0.118702</td>
      <td id="T_802a1_row2_col13" class="data row2 col13">8.707656</td>
      <td id="T_802a1_row2_col14" class="data row2 col14">4.969343</td>
      <td id="T_802a1_row2_col15" class="data row2 col15">2.083895</td>
      <td id="T_802a1_row2_col16" class="data row2 col16">1.488536</td>
      <td id="T_802a1_row2_col17" class="data row2 col17">27.989805</td>
      <td id="T_802a1_row2_col18" class="data row2 col18">0.094467</td>
      <td id="T_802a1_row2_col19" class="data row2 col19">4.143403</td>
      <td id="T_802a1_row2_col20" class="data row2 col20">11.461729</td>
    </tr>
    <tr>
      <th id="T_802a1_level0_row3" class="row_heading level0 row3">min</th>
      <td id="T_802a1_row3_col0" class="data row3 col0">1.000000</td>
      <td id="T_802a1_row3_col1" class="data row3 col1">1989.000000</td>
      <td id="T_802a1_row3_col2" class="data row3 col2">1.000000</td>
      <td id="T_802a1_row3_col3" class="data row3 col3">1.000000</td>
      <td id="T_802a1_row3_col4" class="data row3 col4">1.000000</td>
      <td id="T_802a1_row3_col5" class="data row3 col5">1.000000</td>
      <td id="T_802a1_row3_col6" class="data row3 col6">0.000000</td>
      <td id="T_802a1_row3_col7" class="data row3 col7">0.000000</td>
      <td id="T_802a1_row3_col8" class="data row3 col8">0.000000</td>
      <td id="T_802a1_row3_col9" class="data row3 col9">0.000000</td>
      <td id="T_802a1_row3_col10" class="data row3 col10">0.000000</td>
      <td id="T_802a1_row3_col11" class="data row3 col11">0.000000</td>
      <td id="T_802a1_row3_col12" class="data row3 col12">0.000000</td>
      <td id="T_802a1_row3_col13" class="data row3 col13">0.000000</td>
      <td id="T_802a1_row3_col14" class="data row3 col14">0.000000</td>
      <td id="T_802a1_row3_col15" class="data row3 col15">0.000000</td>
      <td id="T_802a1_row3_col16" class="data row3 col16">0.000000</td>
      <td id="T_802a1_row3_col17" class="data row3 col17">-1.700000</td>
      <td id="T_802a1_row3_col18" class="data row3 col18">-1.264000</td>
      <td id="T_802a1_row3_col19" class="data row3 col19">-52.000000</td>
      <td id="T_802a1_row3_col20" class="data row3 col20">-8.500000</td>
    </tr>
    <tr>
      <th id="T_802a1_level0_row4" class="row_heading level0 row4">25%</th>
      <td id="T_802a1_row4_col0" class="data row4 col0">481.250000</td>
      <td id="T_802a1_row4_col1" class="data row4 col1">1997.000000</td>
      <td id="T_802a1_row4_col2" class="data row4 col2">15.000000</td>
      <td id="T_802a1_row4_col3" class="data row4 col3">15.000000</td>
      <td id="T_802a1_row4_col4" class="data row4 col4">2.000000</td>
      <td id="T_802a1_row4_col5" class="data row4 col5">72.000000</td>
      <td id="T_802a1_row4_col6" class="data row4 col6">838.000000</td>
      <td id="T_802a1_row4_col7" class="data row4 col7">265.000000</td>
      <td id="T_802a1_row4_col8" class="data row4 col8">128.000000</td>
      <td id="T_802a1_row4_col9" class="data row4 col9">46.000000</td>
      <td id="T_802a1_row4_col10" class="data row4 col10">0.404000</td>
      <td id="T_802a1_row4_col11" class="data row4 col11">0.222000</td>
      <td id="T_802a1_row4_col12" class="data row4 col12">0.659000</td>
      <td id="T_802a1_row4_col13" class="data row4 col13">11.000000</td>
      <td id="T_802a1_row4_col14" class="data row4 col14">3.400000</td>
      <td id="T_802a1_row4_col15" class="data row4 col15">1.700000</td>
      <td id="T_802a1_row4_col16" class="data row4 col16">0.500000</td>
      <td id="T_802a1_row4_col17" class="data row4 col17">0.400000</td>
      <td id="T_802a1_row4_col18" class="data row4 col18">0.030000</td>
      <td id="T_802a1_row4_col19" class="data row4 col19">-3.900000</td>
      <td id="T_802a1_row4_col20" class="data row4 col20">-0.400000</td>
    </tr>
    <tr>
      <th id="T_802a1_level0_row5" class="row_heading level0 row5">50%</th>
      <td id="T_802a1_row5_col0" class="data row5 col0">961.500000</td>
      <td id="T_802a1_row5_col1" class="data row5 col1">2005.000000</td>
      <td id="T_802a1_row5_col2" class="data row5 col2">30.000000</td>
      <td id="T_802a1_row5_col3" class="data row5 col3">30.000000</td>
      <td id="T_802a1_row5_col4" class="data row5 col4">5.000000</td>
      <td id="T_802a1_row5_col5" class="data row5 col5">235.000000</td>
      <td id="T_802a1_row5_col6" class="data row5 col6">4204.000000</td>
      <td id="T_802a1_row5_col7" class="data row5 col7">1552.000000</td>
      <td id="T_802a1_row5_col8" class="data row5 col8">656.000000</td>
      <td id="T_802a1_row5_col9" class="data row5 col9">257.000000</td>
      <td id="T_802a1_row5_col10" class="data row5 col10">0.435000</td>
      <td id="T_802a1_row5_col11" class="data row5 col11">0.317000</td>
      <td id="T_802a1_row5_col12" class="data row5 col12">0.736000</td>
      <td id="T_802a1_row5_col13" class="data row5 col13">17.700000</td>
      <td id="T_802a1_row5_col14" class="data row5 col14">6.200000</td>
      <td id="T_802a1_row5_col15" class="data row5 col15">2.800000</td>
      <td id="T_802a1_row5_col16" class="data row5 col16">1.100000</td>
      <td id="T_802a1_row5_col17" class="data row5 col17">5.300000</td>
      <td id="T_802a1_row5_col18" class="data row5 col18">0.069000</td>
      <td id="T_802a1_row5_col19" class="data row5 col19">-2.000000</td>
      <td id="T_802a1_row5_col20" class="data row5 col20">0.000000</td>
    </tr>
    <tr>
      <th id="T_802a1_level0_row6" class="row_heading level0 row6">75%</th>
      <td id="T_802a1_row6_col0" class="data row6 col0">1441.750000</td>
      <td id="T_802a1_row6_col1" class="data row6 col1">2013.000000</td>
      <td id="T_802a1_row6_col2" class="data row6 col2">44.000000</td>
      <td id="T_802a1_row6_col3" class="data row6 col3">44.000000</td>
      <td id="T_802a1_row6_col4" class="data row6 col4">10.000000</td>
      <td id="T_802a1_row6_col5" class="data row6 col5">584.000000</td>
      <td id="T_802a1_row6_col6" class="data row6 col6">13246.000000</td>
      <td id="T_802a1_row6_col7" class="data row6 col7">5150.000000</td>
      <td id="T_802a1_row6_col8" class="data row6 col8">2139.000000</td>
      <td id="T_802a1_row6_col9" class="data row6 col9">910.000000</td>
      <td id="T_802a1_row6_col10" class="data row6 col10">0.474000</td>
      <td id="T_802a1_row6_col11" class="data row6 col11">0.356000</td>
      <td id="T_802a1_row6_col12" class="data row6 col12">0.797000</td>
      <td id="T_802a1_row6_col13" class="data row6 col13">24.800000</td>
      <td id="T_802a1_row6_col14" class="data row6 col14">10.000000</td>
      <td id="T_802a1_row6_col15" class="data row6 col15">4.200000</td>
      <td id="T_802a1_row6_col16" class="data row6 col16">2.100000</td>
      <td id="T_802a1_row6_col17" class="data row6 col17">24.500000</td>
      <td id="T_802a1_row6_col18" class="data row6 col18">0.104000</td>
      <td id="T_802a1_row6_col19" class="data row6 col19">-0.300000</td>
      <td id="T_802a1_row6_col20" class="data row6 col20">4.500000</td>
    </tr>
    <tr>
      <th id="T_802a1_level0_row7" class="row_heading level0 row7">max</th>
      <td id="T_802a1_row7_col0" class="data row7 col0">1922.000000</td>
      <td id="T_802a1_row7_col1" class="data row7 col1">2021.000000</td>
      <td id="T_802a1_row7_col2" class="data row7 col2">60.000000</td>
      <td id="T_802a1_row7_col3" class="data row7 col3">60.000000</td>
      <td id="T_802a1_row7_col4" class="data row7 col4">22.000000</td>
      <td id="T_802a1_row7_col5" class="data row7 col5">1541.000000</td>
      <td id="T_802a1_row7_col6" class="data row7 col6">52139.000000</td>
      <td id="T_802a1_row7_col7" class="data row7 col7">37062.000000</td>
      <td id="T_802a1_row7_col8" class="data row7 col8">15091.000000</td>
      <td id="T_802a1_row7_col9" class="data row7 col9">12091.000000</td>
      <td id="T_802a1_row7_col10" class="data row7 col10">1.000000</td>
      <td id="T_802a1_row7_col11" class="data row7 col11">1.000000</td>
      <td id="T_802a1_row7_col12" class="data row7 col12">1.000000</td>
      <td id="T_802a1_row7_col13" class="data row7 col13">41.100000</td>
      <td id="T_802a1_row7_col14" class="data row7 col14">27.200000</td>
      <td id="T_802a1_row7_col15" class="data row7 col15">13.300000</td>
      <td id="T_802a1_row7_col16" class="data row7 col16">9.500000</td>
      <td id="T_802a1_row7_col17" class="data row7 col17">249.500000</td>
      <td id="T_802a1_row7_col18" class="data row7 col18">1.442000</td>
      <td id="T_802a1_row7_col19" class="data row7 col19">51.100000</td>
      <td id="T_802a1_row7_col20" class="data row7 col20">142.600000</td>
    </tr>
  </tbody>
</table>

使用describe()函数来生成关于数据的描述性统计信息，包括球员各项数值的计数、均值、标准差、最小值、25%分位数、50%分位数、75%分位数和最大值。

```
plt.figure(figsize = (20,10))
sns.countplot(data=df,x="year");
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/d91b0585-ac69-45d5-96d4-7314a79e8d84)

统计1989-2021年每年参加选秀的球员人数。NBA规定每年选秀60人，但有些年份出现了特殊情况(比如球队被没收选秀权等)。
## 相关性分析
接下来我们通过绘制图像分析选秀顺位高低与球员综合实力间的相关关系。
### 总得分与选秀顺位间的关系
```
df0 = df[df["games"] > 250]

fig = px.scatter_3d(df0, x = "year", y = "overall_pick", z = "points", 
                    opacity = 0.75, hover_data = ["player"],
                    color = "overall_pick", color_continuous_scale = "haline_r")

fig.update_traces(marker = dict(size = 3.5)) # scaling down the markers
fig.update_layout(template = "plotly_dark", font = dict(family = "PT Sans", size = 12))
fig.show()
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/a08d449a-1d1e-4f64-85bc-a8c96e271290)

对数据集中满足比赛场数大于250场的球员绘制3d散点图，其中x轴表示年份（"year"列），y轴表示选秀顺位（"overall_pick"列），z轴表示得分（"points"列）。可以看出总体上球员选秀顺位越高，生涯总得分也相应越高。

### 场均得分与选秀顺位间的关系
```
df0 = df[df["games"] > 0]

sorted_df = df0.sort_values(by = "overall_pick", ascending = True)

fig = px.scatter_3d(sorted_df, x = "games", y = "year", z = "points_per_game",
                    range_x = (0, 1500), range_z = (0, 30),
                    hover_data = ["player"], animation_frame = "overall_pick", 
                    range_color = (0, 25), color = "points_per_game", color_continuous_scale = "jet")

fig.update_traces(marker = dict(size = 5)) # scaling down the markers
fig.update_layout(template = "plotly_dark", font = dict(family = "PT Sans", size = 12))
fig.show()
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/9e46312b-025e-405f-ab13-b74b8b768bb0)

相比于总得分，球员的场均得分或许更能直观地体现球员的得分能力与进攻效率。按选秀顺位绘制球员场均得分散点图，我们便能发现，总的来看，高顺位球员在场均得分方面的确优于低顺位球员。然而，即便是每年的状元秀(首轮第1顺位被选中)，仍有球员表现平庸；与此同时，有的球员虽然选秀顺位不高，但其得分能力依然能名列前茅。我们可以认为这种球员的数据为**异常点**。

为了更直观细致地进行数据的横向和纵向对比，我们可以绘制球员数值的特征矩阵。

```
fig = px.scatter(df, x = "overall_pick", y = "year", hover_data = ["player", "team"],
                 color = "points_per_game", color_continuous_scale = "Jet",
                 title = f"NBA Draft Points Per Game by Year and Overall Pick")

fig.update_traces(marker = dict(size = 8, symbol = "square")) # scaling the markers
fig.update_layout(template = "plotly_dark", font = dict(family = "PT Sans", size = 20))
fig.show()
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/e8b113a8-2324-4e1c-8489-595aa0836dc3)

```
fig = px.scatter(df, x = "overall_pick", y = "year", hover_data = ["player", "team"],
                 color = "average_minutes_played", color_continuous_scale = "Jet",
                 title = f"NBA Draft Average Minutes Played by Year and Overall Pick")

fig.update_traces(marker = dict(size = 8, symbol = "square")) # scaling the markers
fig.update_layout(template = "plotly_dark", font = dict(family = "PT Sans", size = 20))
fig.show()
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/2a1e9c55-d5d8-408b-8c7a-44beee6e176a)

以上2张图反映了球员的场均得分与场均上场时间与选秀顺位和选秀年份之间的关系。从中我们可以看到异常数据点的分布情况。

## 异常情况分析

## 构建预测模型
在分析完球员数据的异常分布情况后，我们可以尝试构建模型以实现通过选秀顺位来预测球员的球场表现。

```
X = df[['rank']]
y_points = df['points_per_game']
y_minutes = df['average_minutes_played']

X_train, X_test, y_train_points, y_test_points = train_test_split(X, y_points, test_size=0.5, random_state=23)
X_train, X_test, y_train_minutes, y_test_minutes = train_test_split(X, y_minutes, test_size=0.5, random_state=23)

model_points = LinearRegression()
model_minutes = LinearRegression()

model_points.fit(X_train, y_train_points)
model_minutes.fit(X_train, y_train_minutes)

y_pred_points = model_points.predict(X_test)
y_pred_minutes = model_minutes.predict(X_test)

accuracy_points = mean_squared_error(y_test_points, y_pred_points)
accuracy_minutes = mean_squared_error(y_test_minutes, y_pred_minutes)

mae_points = mean_absolute_error(y_test_points, y_pred_points)
mae_minutes = mean_absolute_error(y_test_minutes, y_pred_minutes)

print("场均得分均方误差:",accuracy_points)
print("场均上场时间均方误差:",accuracy_minutes)
print("场均得分平均绝对误差:",mae_points)
print("场均上场时间平均绝对误差:",mae_minutes)
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/544bf4f1-926e-469e-b9cd-85accd3819ad)

构建2个线性回归模型分别用于预测球员场均得分(points_per_game)和场均出场时间(average_minutes_played)。根据选秀顺位(rank)训练模型，并返回预测模型的均方误差和平均绝对误差。
