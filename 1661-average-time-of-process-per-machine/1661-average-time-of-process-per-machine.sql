# Write your MySQL query statement below
Select start.machine_id , 
Round(AVG(end.timestamp - start.timestamp),3) as processing_time
From Activity as start
Join Activity as end
ON start.machine_id = end.machine_id
AND start.process_id = end.process_id
AND start.activity_type = "start"
AND end.activity_type = "end"
Group by start.machine_id

