# Write your MySQL query statement below

with aa as (
    select
        *,
        max(end_day) over (partition by hall_id order by start_day) as end_day_max
    from
        HallEvents
)
, bb as (
    select
        hall_id,
        start_day,
        end_day,
        lag(end_day_max) over (partition by hall_id order by start_day) as end_day_max_prev
    from
        aa
)
, cc as (
    select
        hall_id,
        start_day,
        end_day,
        sum(if(start_day <= end_day_max_prev, 0, 1)) over (partition by hall_id order by start_day) as overlap_group
    from
        bb
)
select
    hall_id,
    min(start_day) as start_day,
    max(end_day) as end_day
from 
    cc
group by
    hall_id, overlap_group
order by
    hall_id, overlap_group
