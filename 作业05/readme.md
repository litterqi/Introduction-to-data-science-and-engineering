##第6章：


##第7章：

#第4题：
```
SELECT * 
FROM user
WHERE age BETWEEN 20 AND 30;
```
#第5题：
```
DELETE FROM user 
WHERE name LIKE '%张%';
```
#第6题：
```
SELECT AVG(age) AS average_age
FROM user;
```
#第7题：
```
SELECT *
FROM user
WHERE age BETWEEN 20 AND 30 AND name LIKE '%张%'
ORDER BY age DESC;
```
#第9题：
```
SELECT user.*
FROM score
INNER JOIN team ON score.teamid = team.id
INNER JOIN user ON score.userid = user.id
WHERE team.teamName = 'ECNU' AND user.age < 20;
```
#第10题：
```
SELECT team.teamName, COALESCE(SUM(score.score), 0) AS totalScore
FROM score
INNER JOIN team ON score.teamid = team.id
WHERE team.teamName = 'ECNU'
GROUP BY team.teamName;
```
