# Write your MySQL query statement below
select w1.id 
From Weather as w1
Join Weather as w2
ON Datediff(w1.recorddate,w2.recorddate) = 1
Where w1.temperature > w2.temperature