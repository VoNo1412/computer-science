select * from Weather w
join Weather prev on w.recordDate = prev.recordDate + INTERVAL 1 DAY
where w.temperature > prev.temperature
order by w.recordDate asc