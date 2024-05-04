{{ config(materialized='table') }}

select
    type,
    sum(traveled_d) as total_distance_traveled
from
    vehicle
GROUP BY
    type