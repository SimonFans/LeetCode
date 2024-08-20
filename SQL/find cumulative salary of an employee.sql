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
