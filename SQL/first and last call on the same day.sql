https://leetcode.com/problems/first-and-last-call-on-the-same-day/
  
with calling as (
    select caller_id as user_id, recipient_id as pair_id, call_time from Calls
    union all
    select recipient_id as user_id, caller_id as pair_id, call_time from Calls   
), first_last_call as (
    select *,
    first_value(pair_id) over (partition by user_id, date(call_time) order by call_time) as first_call_person,
    first_value(pair_id) over (partition by user_id, date(call_time) order by call_time desc) as last_call_person
    from calling
)
select distinct user_id from first_last_call
where first_call_person = last_call_person


  // for each user_id, who he calls to the first and the last
| user_id | pair_id | call_time           | first_call_person | last_call_person |
| ------- | ------- | ------------------- | ----------------- | ---------------- |
| 1       | 5       | 2021-08-11 05:28:44 | 5                 | 5                |
| 3       | 11      | 2021-08-17 13:07:00 | 8                 | 11               |
| 3       | 8       | 2021-08-17 04:04:15 | 8                 | 11               |
| 4       | 8       | 2021-08-24 19:57:13 | 8                 | 8                |
| 4       | 8       | 2021-08-24 17:46:07 | 8                 | 8                |
| 5       | 1       | 2021-08-11 05:28:44 | 1                 | 1                |
| 8       | 11      | 2021-08-17 22:22:22 | 3                 | 11               |
| 8       | 3       | 2021-08-17 04:04:15 | 3                 | 11               |
| 8       | 4       | 2021-08-24 19:57:13 | 4                 | 4                |
| 8       | 4       | 2021-08-24 17:46:07 | 4                 | 4                |
