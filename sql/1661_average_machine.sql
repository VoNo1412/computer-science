select s.machine_id, ROUND(sum((e.end_time - s.start_time) / count(s.machine_id)), 3) 
from (
    select machine_id, process_id, timestamp as start_time from Activity where activity_type = "start"
) s
join (
    select machine_id, process_id, timestamp as end_time from Activity where activity_type = "end"
) e on e.machine_id = s.machine_id and e.process_id = s.process_id
group by s.machine_id