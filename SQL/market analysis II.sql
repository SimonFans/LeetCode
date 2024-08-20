https://leetcode.com/problems/market-analysis-ii/

# Write your MySQL query statement below

with seller_items as (
    select
       seller_id,
       item_id,
       row_number() over (partition by seller_id order by order_date) as rn
    from orders
)
, seller_second_item as (
    select 
      seller_id,
      item_id
    from seller_items
    where rn = 2
) 
select 
  u.user_id as seller_id,
  case when u.favorite_brand != i.item_brand or i.item_brand is null then 'no' 
       else 'yes' 
  end as 2nd_item_fav_brand
from users as u
left join seller_second_item as s
on u.user_id = s.seller_id
left join items as i
on s.item_id = i.item_id

