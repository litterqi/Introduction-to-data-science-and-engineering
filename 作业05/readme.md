# 第五周作业
## 第6章：

### 第1题：

[movie.csv](https://github.com/litterqi/Introduction-to-data-science-and-engineering/blob/%E4%BD%9C%E4%B8%9A/%E4%BD%9C%E4%B8%9A05/movie.csv)

### 第2题：

scrapy框架的优缺点：

优点:

1.快速: scrapy具有处理各种网络爬虫任务的高效性能，并可以快速地从目标网站抓取数据。

2.可扩展性: scrapy支持多种插件，包括下载中间件、存储管道和扩展，使得开发者能够根据自己的需求扩展其功能。

3.完整的功能: scrapy具有完整的功能集合，包括自动重试、自定义请求头、代理管理、cookie管理等，可用于完成各种复杂的网络爬虫任务。

4.强大的选择器: scrapy使用强大的CSS选择器和XPath选择器来定位页面上的元素，帮助用户方便地提取所需数据。

缺点:

1.学习成本高: scrapy需要熟悉一定的Python语言基础和HTML语言知识，因此学习成本较高。

2.资源占用高: scrapy运行时需要占用较高的系统资源，特别是在大规模抓取时可能会占用更多系统资源。

3.运行缓慢: scrapy需要启动和配置操作，而且需要大量的I/O操作来加载和分析页面上的数据，因此可能运行较慢。

4.反爬虫机制：一些网站会采取反爬虫策略，如设置访问速率限制、页面解析难度提高等，这会增加爬取的难度，需要采取相应的策略和技术来应对。
### 第3题：

[mySpider](https://github.com/litterqi/Introduction-to-data-science-and-engineering/tree/%E4%BD%9C%E4%B8%9A/%E4%BD%9C%E4%B8%9A05/mySpider)

### 第4题：

[computer_science.html](https://github.com/litterqi/Introduction-to-data-science-and-engineering/blob/%E4%BD%9C%E4%B8%9A/%E4%BD%9C%E4%B8%9A05/computer_science.html)

### 第5题：

[dangdangbook.csv](https://github.com/litterqi/Introduction-to-data-science-and-engineering/blob/%E4%BD%9C%E4%B8%9A/%E4%BD%9C%E4%B8%9A05/dangdangbook.csv)

## 第7章：

### 第2题：
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/728e6f39-dc3b-441a-9a63-e4e12af78b0a)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/b6f26bab-0f5e-4d9b-a1cc-23e769fb0ca5)

### 第3题：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/396fe575-4a88-45ba-a346-f9f4e8652070)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/d06f580d-3f0c-43ea-a9e2-a339acb0f37d)

### 第4题：
```
SELECT * FROM user WHERE age BETWEEN 20 AND 30;
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/661ade1e-2d67-4c59-987a-32b641749f83)

### 第5题：
```
DELETE FROM user WHERE name LIKE '%张%';
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/6cee9b6b-a48f-456d-8107-ba7cc23c9a9e)

### 第6题：
```
SELECT AVG(age) AS average_age FROM user;
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/bafd5e29-1ae2-4127-bfea-bd539434d4e1)

### 第7题：
```
SELECT * FROM user WHERE age BETWEEN 20 AND 30 AND name LIKE '%张%' ORDER BY age DESC;
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/ba02b9e4-72b9-467b-8864-1b25bd60a71e)

### 第8题：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/6050abed-1a38-4e36-a394-4f556e8ce7b9)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/0171b0e9-e319-4bce-8ee3-d09c955cd14a)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/12543cb3-e2e8-4108-a296-3cfb70bc197d)

### 第9题：
```
select * from user where id in (select user_id from score where team_id in (select id from team where team_name='ECNU')) and age<20;
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/a023597d-d4b4-48fe-b3e7-594c8584cd93)

### 第10题：
```
select sum(score) from score where team_id in (select id from team where team_name='ECNU');
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/a309aa2f-1450-4fae-815c-51328f5ec078)
