# Write your MySQL query statement below
select 
    s.student_id, 
    s.student_name, 
    sb.subject_name,
    ifnull(ex.exam_count, 0) as attended_exams 
from Students s
cross join Subjects sb
left join (
      SELECT 
            student_id, 
            subject_name, 
            COUNT(*) AS exam_count
        FROM 
            Examinations
        GROUP BY 
            student_id, 
            subject_name
) as ex on ex.student_id = s.student_id and ex.subject_name = sb.subject_name
order by s.student_id, sb.subject_name