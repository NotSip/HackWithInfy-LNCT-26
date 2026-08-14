# Write your MySQL query statement below
Select e.unique_id , l.name
From Employees as l
Left Join EmployeeUNI as e
ON l.id <=> e.id