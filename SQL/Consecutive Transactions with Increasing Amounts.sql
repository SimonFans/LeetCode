# Write your MySQL query statement below
with data1 as (
  select 
    a.customer_id,
    a.transaction_date
  from Transactions a
  inner join Transactions b
  on a.customer_id = b.customer_id
  and b.amount > a.amount
  and datediff(b.transaction_date, a.transaction_date) = 1
)
, data2 as (
    select 
      customer_id,
      transaction_date,
      row_number() over (partition by customer_id order by transaction_date) as rn
    from data1
)
, data3 as (
    select
      customer_id,
      transaction_date,
      date_sub(transaction_date, interval rn day) as data_group
    from data2
)
, data4 as (
    select
      customer_id,
      min(transaction_date) as consecutive_start,
      count(*) as cnt
    from data3
    group by customer_id, data_group
)
select
  customer_id,
  consecutive_start,
  date_add(consecutive_start, interval cnt day) as consecutive_end
from data4
where cnt > 1
order by customer_id

