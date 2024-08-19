# get the valid client and driver
with valid_trips as (
   select 
      t.request_at,
      sum(case when t.status != 'completed' then 1 else 0 end) as cancelled_sum,
      count(*) as requests_count
   from trips as t
   join users as client
   on t.client_id = client.users_id
   join users as driver
   on t.driver_id = driver.users_id
   where (request_at between '2013-10-01' and '2013-10-03') and (client.banned = 'No' and driver.banned = 'No')
   group by t.request_at
)
select 
   request_at as Day,
   round(cancelled_sum/requests_count, 2) as "cancellation rate"
from valid_trips
