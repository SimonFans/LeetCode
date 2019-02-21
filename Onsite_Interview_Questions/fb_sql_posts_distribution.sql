Find post distribution

your answer should look like: (评论有十条的有几个，有二十条的有几个,target_id是回复哪个帖子Id)

comments=10  frequency=2
comments=20  frequency=3

                    Table story

user_id	  content_id	  date	    content_type	  target_id
  22	       1234	     2/1/2015	   photo	        null
  13	       3456	     2/1/2015	   comment	      1234
  47	       5678	     2/1/2015	   comment	      1234
  86	       2000	     2/3/2015	   video	        null
  87	       2100	     2/4/2015	   comment	      2000
  88	       2200	     2/5/2015	   comment	      2000


select comment_nums as comments, count(Id) as frequency
from
(
select a.content_id as Id, count(b.content_id) as comment_nums
from story a left join story b
on a.content_id=b.target_id
where a.content_type in ('photo','video')
and b.content_type='comment'
group by a.content_id 
) tmp
group by comment_nums
