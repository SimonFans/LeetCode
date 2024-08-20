Input: 
Orders table:
+------------+--------------+-------------+--------------+-------------+
| order_id   | customer_id  | order_date  | item_id      | quantity    |
+------------+--------------+-------------+--------------+-------------+
| 1          | 1            | 2020-06-01  | 1            | 10          |
| 2          | 1            | 2020-06-08  | 2            | 10          |
| 3          | 2            | 2020-06-02  | 1            | 5           |
| 4          | 3            | 2020-06-03  | 3            | 5           |
| 5          | 4            | 2020-06-04  | 4            | 1           |
| 6          | 4            | 2020-06-05  | 5            | 5           |
| 7          | 5            | 2020-06-05  | 1            | 10          |
| 8          | 5            | 2020-06-14  | 4            | 5           |
| 9          | 5            | 2020-06-21  | 3            | 5           |
+------------+--------------+-------------+--------------+-------------+
Items table:
+------------+----------------+---------------+
| item_id    | item_name      | item_category |
+------------+----------------+---------------+
| 1          | LC Alg. Book   | Book          |
| 2          | LC DB. Book    | Book          |
| 3          | LC SmarthPhone | Phone         |
| 4          | LC Phone 2020  | Phone         |
| 5          | LC SmartGlass  | Glasses       |
| 6          | LC T-Shirt XL  | T-Shirt       |
+------------+----------------+---------------+
Output: 
+------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Category   | Monday    | Tuesday   | Wednesday | Thursday  | Friday    | Saturday  | Sunday    |
+------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Book       | 20        | 5         | 0         | 0         | 10        | 0         | 0         |
| Glasses    | 0         | 0         | 0         | 0         | 5         | 0         | 0         |
| Phone      | 0         | 0         | 5         | 1         | 0         | 0         | 10        |
| T-Shirt    | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
+------------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+

select b.item_category as 'CATEGORY', sum(case when weekday(a.order_date) = 0 then a.quantity else 0 end) as 'MONDAY',
sum(case when weekday(a.order_date) = 1 then a.quantity else 0 end) as 'TUESDAY',
sum(case when weekday(a.order_date) = 2 then a.quantity else 0 end) as 'WEDNESDAY',
sum(case when weekday(a.order_date) = 3 then a.quantity else 0 end) as 'THURSDAY',
sum(case when weekday(a.order_date) = 4 then a.quantity else 0 end) as 'FRIDAY',
sum(case when weekday(a.order_date) = 5 then a.quantity else 0 end) as 'SATURDAY',
sum(case when weekday(a.order_date) = 6 then a.quantity else 0 end) as 'SUNDAY'
from items b left join orders a on a.item_id = b.item_id
group by b.item_category
order by b.item_category
