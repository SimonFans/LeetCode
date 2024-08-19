# Write your MySQL query statement below

with unqiue_users as (
  select
        user1 as user
    from Friends
    union 
    select 
       user2 as user
    from Friends
)
, total_number_online as (
    select
      count(*) as number_users_platform
    from unqiue_users
)
, unique_user_friends_count as (
    select 
     user,
     count(distinct user_friends) as user_friends_cnt
    from (
    select
      uu.user,
      f1.user2 as user_friends
    from unqiue_users as uu
    left join Friends as f1
    on uu.user = f1.user1
    where f1.user2 is not null
    union all
    select
      uu.user,
      f2.user1 as user_friends
    from unqiue_users as uu
    left join Friends as f2
    on uu.user = f2.user2
    where f2.user1 is not null
    ) t
    group by user  
)
select 
    user as user1,
    round(user_friends_cnt/(select number_users_platform from total_number_online) *100,2) as percentage_popularity
from unique_user_friends_count
order by user1
