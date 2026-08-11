# Write your MySQL query statement below   
Select Max(salary) as SecondHighestSalary
From Employee
Where salary<(select Max(salary) From Employee)