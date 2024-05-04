{{ config(materialized='table') }}

select
    time as hour_of_day,
    count(*) as number_of_vehicles
from
    trajectories
GROUP BY
    hour_of_day
order by 
    hour_of_day
limit 5
    