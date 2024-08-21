# Write your MySQL query statement below

with date_platform as (
    select distinct spend_date, 'desktop' platform from spending 
      union all
    select distinct spend_date, 'mobile' platform from spending 
      union all
    select distinct spend_date, 'both' platform from spending
)
, user_date as (
    select
      user_id,
      spend_date,
      case when count(*) = 1 then platform else 'both' end as platform,
      sum(amount) as amount
    from spending
    group by user_id, spend_date
)
select
   dp.spend_date,
   dp.platform,
   sum(coalesce(amount,0)) as total_amount,
   sum(case when amount is null then 0 else 1 end) as total_users
from date_platform as dp
left join user_date as u
on dp.spend_date = u.spend_date and dp.platform = u.platform
group by dp.spend_date, dp.platform
