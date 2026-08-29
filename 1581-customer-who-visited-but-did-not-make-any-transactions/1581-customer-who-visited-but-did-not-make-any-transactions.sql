# Write your MySQL query statement below
select v.customer_id , count(v.visit_id) as count_no_trans
From Visits v 
Left join Transactions t
ON v.visit_id = t.visit_id
Where t.transaction_id IS NULL
Group by v.customer_id
