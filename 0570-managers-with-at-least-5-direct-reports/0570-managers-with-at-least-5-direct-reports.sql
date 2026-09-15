# Write your MySQL query statement below
Select t1.name
From Employee as t1
Join Employee as t2
On t1.id = t2.managerId
group by t2.managerId 
having Count(t2.managerId) >= 5
