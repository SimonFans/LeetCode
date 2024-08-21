Write a solution to calculate the cumulative salary summary for every employee in a single unified table.

The cumulative salary summary for an employee can be calculated as follows:

For each month that the employee worked, sum up the salaries in that month and the previous two months. This is their 3-month sum for that month. If an employee did not work for the company in previous months, their effective salary for those months is 0.
Do not include the 3-month sum for the most recent month that the employee worked for in the summary.
Do not include the 3-month sum for any month the employee did not work.
Return the result table ordered by id in ascending order. In case of a tie, order it by month in descending order.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+-------+--------+
| id | month | salary |
+----+-------+--------+
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 1  | 2     | 30     |
| 2  | 2     | 30     |
| 3  | 2     | 40     |
| 1  | 3     | 40     |
| 3  | 3     | 60     |
| 1  | 4     | 60     |
| 3  | 4     | 70     |
| 1  | 7     | 90     |
| 1  | 8     | 90     |
+----+-------+--------+
Output: 
+----+-------+--------+
| id | month | Salary |
+----+-------+--------+
| 1  | 7     | 90     |
| 1  | 4     | 130    |
| 1  | 3     | 90     |
| 1  | 2     | 50     |
| 1  | 1     | 20     |
| 2  | 1     | 20     |
| 3  | 3     | 100    |
| 3  | 2     | 40     |
+----+-------+--------+

with cte as (
select 
  e1.id,
  e1.month,
  e1.salary,
--   e2.month,
  coalesce(e2.salary, 0) as prev_one_salary,
--   e3.month,
  coalesce(e3.salary, 0) as  prev_two_salary
from employee as e1
left join employee as e2
on e1.id = e2.id and e1.month - 1 = e2.month
left join employee as e3
on e2.id = e3.id and e2.month - 1 = e3.month
)
, exclude_most_recent_month as (
    select
      id,
      max(month) as most_recent_month
    from employee
    group by id
)
select
  cte.id,
  cte.month,
  cte.salary + cte.prev_one_salary + cte.prev_two_salary as salary
from cte
inner join exclude_most_recent_month as e on cte.id = e.id
where cte.month != e.most_recent_month
order by id asc, month desc
