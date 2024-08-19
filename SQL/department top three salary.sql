with rank_salary as (
   select 
     departmentId,
     name,
     salary,
     dense_rank() over (partition by departmentId order by salary desc) as rk
   from employee
)
select 
   d.name as Department,
   r.name as Employee,
   r.Salary
from rank_salary as r
join department as d
on r.departmentId = d.id
where rk <= 3
