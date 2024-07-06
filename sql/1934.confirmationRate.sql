select 
    s.user_id,
    ifnull(c.confirmed / (c.confirmed + c.timeout), 0) as confirmations_rate
from Signups s
left join (
    select 
        (case when action = "confirmed" then 1 else 0 end) as confirmed,
        sum(case when action = "timeout" then 1 else 0 end) as timeout,
        user_id
    from Confirmations
    group by user_id
) c on c.user_id = s.user_id
order by confirmations_rate
