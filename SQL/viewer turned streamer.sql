# Write your MySQL query statement below

with user_sessions as (
    select
      user_id,
      session_type,
      row_number() over (partition by user_id order by session_start) as rn
    from sessions 
)
, get_valid_user_id as (
    select
      user_id 
    from user_sessions
    where rn = 1 and session_type = 'Viewer'
)
, valid_data as (
  select 
     u.user_id,
     sum(case when s.session_type = 'Streamer' then 1 else 0 end) as sessions_count
  from get_valid_user_id as u
  join sessions as s
  on u.user_id = s.user_id
  group by u.user_id
)
select * from valid_data
where sessions_count != 0
order by sessions_count desc, user_id desc
