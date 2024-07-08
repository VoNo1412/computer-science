select 
query_name,
ROUND((sum(rating / position)) / count(*), 2) as quality,
ROUND((sum(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / count(*)) * 100, 2) as poor_query_percentage 
from Queries
where query_name is not null
group by query_name
