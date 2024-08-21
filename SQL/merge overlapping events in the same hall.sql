Write a solution to merge all the overlapping events that are held in the same hall. Two events overlap if they have at least one day in common.

Return the result table in any order.

The result format is in the following example.

 
Example 1:

Input: 
HallEvents table:
+---------+------------+------------+
| hall_id | start_day  | end_day    |
+---------+------------+------------+
| 1       | 2023-01-13 | 2023-01-14 |
| 1       | 2023-01-14 | 2023-01-17 |
| 1       | 2023-01-18 | 2023-01-25 |
| 2       | 2022-12-09 | 2022-12-23 |
| 2       | 2022-12-13 | 2022-12-17 |
| 3       | 2022-12-01 | 2023-01-30 |
+---------+------------+------------+
Output: 
+---------+------------+------------+
| hall_id | start_day  | end_day    |
+---------+------------+------------+
| 1       | 2023-01-13 | 2023-01-17 |
| 1       | 2023-01-18 | 2023-01-25 |
| 2       | 2022-12-09 | 2022-12-23 |
| 3       | 2022-12-01 | 2023-01-30 |
+---------+------------+------------+
Explanation: There are three halls.
Hall 1:
- The two events ["2023-01-13", "2023-01-14"] and ["2023-01-14", "2023-01-17"] overlap. We merge them in one event ["2023-01-13", "2023-01-17"].
- The event ["2023-01-18", "2023-01-25"] does not overlap with any other event, so we leave it as it is.
Hall 2:
- The two events ["2022-12-09", "2022-12-23"] and ["2022-12-13", "2022-12-17"] overlap. We merge them in one event ["2022-12-09", "2022-12-23"].
Hall 3:
- The hall has only one event, so we return it. Note that we only consider the events of each hall separately.


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
