{{ config(materialized='table') }}

select
    time as hour_of_day,
    AVG(speed) as average_speed
from
    trajectories
GROUP by
    hour_of_day
order by
    hour_of_day