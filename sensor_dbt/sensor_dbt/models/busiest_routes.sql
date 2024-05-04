{{ config(materialized='table') }}

select
    concat(lat, ',', lon) as route,
    count(*) as number_of_vehicles
from 
    trajectories
GROUP by
    route
order by
    number_of_vehicles desc

