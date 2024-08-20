# Write your MySQL query statement below

with avg_dept_salary_per_month as (
  select 
    DATE_FORMAT(pay_date, '%Y-%m') AS pay_month,
    e.department_id,
    avg(s.amount) as avg_dept_salary
  from salary as s
  inner join employee as e
  on s.employee_id  = e.employee_id
  group by DATE_FORMAT(pay_date, '%Y-%m'), e.department_id
)
, avg_company_salary_per_month as (
  select 
    DATE_FORMAT(pay_date, '%Y-%m') AS pay_month,
    avg(amount) as avg_company_salary
  from salary
  group by DATE_FORMAT(pay_date, '%Y-%m')
)
select 
    d.pay_month,
    d.department_id,
    case when d.avg_dept_salary < c.avg_company_salary then 'lower'
         when d.avg_dept_salary > c.avg_company_salary then 'higher'
         else 'same'
    end as comparison
from avg_dept_salary_per_month as d
inner join avg_company_salary_per_month as c
on d.pay_month = c.pay_month
