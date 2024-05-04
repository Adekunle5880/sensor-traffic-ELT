{{ config(materialized='table') }}

SELECT 
    concat(lat, ',', lon) as route,
    AVG(speed) as average_speed
from
    trajectories
GROUP by
    route
order by
    average_speed