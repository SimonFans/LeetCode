Write a solution to find the total number of users and the total amount spent using the mobile only, the desktop only, and both mobile and desktop together for each date.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Spending table:
+---------+------------+----------+--------+
| user_id | spend_date | platform | amount |
+---------+------------+----------+--------+
| 1       | 2019-07-01 | mobile   | 100    |
| 1       | 2019-07-01 | desktop  | 100    |
| 2       | 2019-07-01 | mobile   | 100    |
| 2       | 2019-07-02 | mobile   | 100    |
| 3       | 2019-07-01 | desktop  | 100    |
| 3       | 2019-07-02 | desktop  | 100    |
+---------+------------+----------+--------+
Output: 
+------------+----------+--------------+-------------+
| spend_date | platform | total_amount | total_users |
+------------+----------+--------------+-------------+
| 2019-07-01 | desktop  | 100          | 1           |
| 2019-07-01 | mobile   | 100          | 1           |
| 2019-07-01 | both     | 200          | 1           |
| 2019-07-02 | desktop  | 100          | 1           |
| 2019-07-02 | mobile   | 100          | 1           |
| 2019-07-02 | both     | 0            | 0           |
+------------+----------+--------------+-------------+ 
Explanation: 
On 2019-07-01, user 1 purchased using both desktop and mobile, user 2 purchased using mobile only and user 3 purchased using desktop only.
On 2019-07-02, user 2 purchased using mobile only, user 3 purchased using desktop only and no one purchased using both platforms.



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
