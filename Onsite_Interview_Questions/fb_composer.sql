Composer table: user_id|date|event(start|post|cancel)
user table: User_id|date|country|active (1|0)

1. success rate for post each day for past week?
2. avg number of post for active user today by country?

<1>
select date, sum(case when event='post' then 1 else 0 end)/count(*)
from Composer
where date > DATE_SUB(curdate(), INTERVAL 7 DAY) and date< curdate()
group by date
