# Write your MySQL query statement below

with stu_gpa_meets as (
    select
        student_id
    from enrollments
    group by student_id
    having avg(GPA) >= 2.5
)
, course_content as (
    select
        major,
        sum(case when mandatory = 'yes' then 1 else 0 end) as mandatory_amount
    from courses
    group by major
)
, stu_event as (
    select
       e.student_id,
       c.major,
       sum(case when c.mandatory = 'yes' and e.grade = 'A' then 1 else 0 end) as take_valid_mandatory,
       sum(case when c.mandatory = 'no' and e.grade in ('A', 'B') then 1 else 0 end) as take_valid_elective,
       max(case when c.major = s.major then 1 else 0 end) as is_major_match
    from enrollments as e
    left join courses as c
    on e.course_id = c.course_id
    left join students as s
    on e.student_id = s.student_id
    group by e.student_id, c.major
    
)
select s.student_id
from stu_event as s
left join course_content as c
on s.major = c.major
where s.take_valid_mandatory = c.mandatory_amount and s.take_valid_elective >= 2 
and s.student_id in (select student_id from stu_gpa_meets) and is_major_match = 1
order by student_id
