##第6章：

#第4题：

[computer_science.html](https://github.com/litterqi/Introduction-to-data-science-and-engineering/blob/%E4%BD%9C%E4%B8%9A/%E4%BD%9C%E4%B8%9A05/computer_science.html)

#第5题：

[dangdangbook.csv]

##第7章：

#第2题：
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/728e6f39-dc3b-441a-9a63-e4e12af78b0a)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/b6f26bab-0f5e-4d9b-a1cc-23e769fb0ca5)

#第3题：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/396fe575-4a88-45ba-a346-f9f4e8652070)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/d06f580d-3f0c-43ea-a9e2-a339acb0f37d)

#第4题：
```
SELECT * FROM user WHERE age BETWEEN 20 AND 30;
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/661ade1e-2d67-4c59-987a-32b641749f83)

#第5题：
```
DELETE FROM user WHERE name LIKE '%张%';
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/6cee9b6b-a48f-456d-8107-ba7cc23c9a9e)

#第6题：
```
SELECT AVG(age) AS average_age FROM user;
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/bafd5e29-1ae2-4127-bfea-bd539434d4e1)

#第7题：
```
SELECT * FROM user WHERE age BETWEEN 20 AND 30 AND name LIKE '%张%' ORDER BY age DESC;
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/ba02b9e4-72b9-467b-8864-1b25bd60a71e)

#第8题：

![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/6050abed-1a38-4e36-a394-4f556e8ce7b9)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/0171b0e9-e319-4bce-8ee3-d09c955cd14a)
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/12543cb3-e2e8-4108-a296-3cfb70bc197d)

#第9题：
```
select * from user where id in (select user_id from score where team_id in (select id from team where team_name='ECNU')) and age<20;
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/a023597d-d4b4-48fe-b3e7-594c8584cd93)

#第10题：
```
select sum(score) from score where team_id in (select id from team where team_name='ECNU');
```
![image](https://github.com/litterqi/Introduction-to-data-science-and-engineering/assets/123362884/a309aa2f-1450-4fae-815c-51328f5ec078)
