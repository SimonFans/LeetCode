# Write your MySQL query statement below

with cur_year_spend as (
    select
      year(transaction_date) as year,
      product_id,
      sum(spend) as curr_year_spend
    from user_transactions
    group by year(transaction_date), product_id
)
, cur_prev_year_spend as (
    select
     year,
     product_id,
     curr_year_spend,
     lag(curr_year_spend, 1) over (partition by product_id order by year) as prev_year_spend 
    from cur_year_spend
)
select 
  year,
  product_id,
  curr_year_spend,
  prev_year_spend,
  round((curr_year_spend - prev_year_spend)/prev_year_spend * 100, 2) as yoy_rate 
from cur_prev_year_spend
order by product_id, year
