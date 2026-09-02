# Write your MySQL query statement below
Select e.name , b.bonus
From Employee as e
Left Join Bonus as b
On e.empId = b.empId
Where b.Bonus IS Null
OR b.Bonus < 1000